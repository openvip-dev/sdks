"""High-level OpenVIP client."""

from __future__ import annotations

import json
import logging
import time
import urllib.error
import urllib.request
from typing import Any, Callable, Iterator

from openvip.messages import PROTOCOL_VERSION, create_speech_request
from openvip.models.ack import Ack
from openvip.models.speech_request import SpeechRequest
from openvip.models.speech_response import SpeechResponse
from openvip.models.status import Status
from openvip.models.transcription import Transcription

DEFAULT_URL = "http://localhost:8770"

logger = logging.getLogger(__name__)


class DuplicateAgentError(Exception):
    """Raised when an agent ID is already connected (HTTP 409)."""


class Client:
    """High-level OpenVIP HTTP client.

    Provides a simple API for interacting with an OpenVIP-compatible engine.

    Example::

        from openvip import Client

        client = Client()
        client.speak("Hello world", language="en")
        status = client.get_status()
        print(status.connected_agents)
    """

    def __init__(
        self, url: str = DEFAULT_URL, *, timeout: float = 10.0,
        token: str | None = None,
    ) -> None:
        """Initialize client.

        Args:
            url: Base URL of the OpenVIP engine (default: http://localhost:8770).
            timeout: HTTP request timeout in seconds.
            token: Optional Bearer token for authentication.
        """
        self.url = url.rstrip("/")
        self.timeout = timeout
        self._token = token

    # --- Speech ---

    def speak(
        self, text: str, *, language: str | None = None, **kwargs: Any
    ) -> SpeechResponse:
        """Request text-to-speech synthesis.

        Args:
            text: Text to speak.
            language: BCP 47 language tag (e.g. "en", "it").
            **kwargs: Platform-specific extensions (e.g. engine, voice, speed).
                These are passed through to the server but are not part of the
                OpenVIP protocol specification.

        Returns:
            SpeechResponse with status and duration_ms.
        """
        req = create_speech_request(text, language=language)
        body = req.to_dict()
        if kwargs:
            body.update(kwargs)
        data = self._post("/speech", body)
        return SpeechResponse.from_dict(data)

    # --- Status ---

    def get_status(self) -> Status:
        """Get engine status.

        Returns:
            Status with protocol_version, connected_agents, and platform details.
        """
        data = self._get("/status")
        return Status.from_dict(data)

    def is_available(self) -> bool:
        """Check if the engine is reachable.

        Returns:
            True if the engine responds to a status request, False otherwise.
        """
        try:
            self.get_status()
            return True
        except (ConnectionRefusedError, urllib.error.URLError, OSError):
            return False

    # --- Control ---

    def control(self, command: str) -> Ack:
        """Send a control command.

        Args:
            command: Command string (e.g. "stt.start", "stt.stop", "engine.shutdown").

        Returns:
            Ack response.
        """
        data = self._post("/control", {"command": command})
        return Ack.from_dict(data)

    def start_listening(self) -> Ack:
        """Start speech-to-text."""
        return self.control("stt.start")

    def stop_listening(self) -> Ack:
        """Stop speech-to-text."""
        return self.control("stt.stop")

    def shutdown(self) -> Ack:
        """Request engine shutdown."""
        return self.control("engine.shutdown")

    # --- Messages ---

    def send_message(self, agent_id: str, message: Transcription) -> Ack:
        """Send a message to a connected agent.

        Args:
            agent_id: Target agent identifier.
            message: Transcription message to send.

        Returns:
            Ack response.
        """
        data = self._post(f"/agents/{agent_id}/messages", message.to_dict())
        return Ack.from_dict(data)

    def subscribe(
        self,
        agent_id: str,
        *,
        reconnect: bool = False,
        retry_delay: float = 0.5,
        max_retry_delay: float = 5.0,
        stop: Callable[[], bool] | None = None,
        on_connect: Callable[[], None] | None = None,
        on_disconnect: Callable[[Exception | None], None] | None = None,
    ) -> Iterator[Transcription | SpeechRequest]:
        """Subscribe to messages for an agent via SSE.

        This is a blocking iterator that yields messages as they arrive.
        The SSE connection acts as agent registration — the agent exists
        as long as this iterator is active.

        Args:
            agent_id: Agent identifier to register.
            reconnect: If True, automatically reconnect on connection loss
                with exponential backoff. If False (default), the iterator
                ends when the connection drops.
            retry_delay: Initial delay between reconnection attempts in seconds.
            max_retry_delay: Maximum delay between reconnection attempts.
            stop: Optional callable that returns True to stop the iterator.
                Checked between reconnection attempts.
            on_connect: Optional callback invoked on each successful connection.
            on_disconnect: Optional callback invoked on disconnection, receives
                the exception (or None for clean disconnect).

        Yields:
            Transcription or SpeechRequest messages from the engine.

        Raises:
            DuplicateAgentError: If the agent ID is already connected (HTTP 409).
        """
        url = f"{self.url}/agents/{agent_id}/messages"
        yield from self._sse_stream(
            url,
            self._parse_agent_message,
            reconnect=reconnect,
            retry_delay=retry_delay,
            max_retry_delay=max_retry_delay,
            stop=stop,
            on_connect=on_connect,
            on_disconnect=on_disconnect,
            conflict_message=f"Agent '{agent_id}' is already connected",
        )

    def subscribe_status(
        self,
        *,
        reconnect: bool = False,
        retry_delay: float = 0.5,
        max_retry_delay: float = 5.0,
        stop: Callable[[], bool] | None = None,
        on_connect: Callable[[], None] | None = None,
        on_disconnect: Callable[[Exception | None], None] | None = None,
    ) -> Iterator[Status]:
        """Subscribe to status changes via SSE.

        This is a blocking iterator that yields status updates as they occur.
        Events are sent only on state transitions (e.g. idle → listening,
        agent connect/disconnect). Continuously changing fields like
        uptime_seconds do not trigger events.

        Args:
            reconnect: If True, automatically reconnect on connection loss
                with exponential backoff. If False (default), the iterator
                ends when the connection drops.
            retry_delay: Initial delay between reconnection attempts in seconds.
            max_retry_delay: Maximum delay between reconnection attempts.
            stop: Optional callable that returns True to stop the iterator.
                Checked between reconnection attempts.
            on_connect: Optional callback invoked on each successful connection.
            on_disconnect: Optional callback invoked on disconnection, receives
                the exception (or None for clean disconnect).

        Yields:
            Status objects on each state change.
        """
        url = f"{self.url}/status/stream"
        yield from self._sse_stream(
            url,
            Status.from_dict,
            reconnect=reconnect,
            retry_delay=retry_delay,
            max_retry_delay=max_retry_delay,
            stop=stop,
            on_connect=on_connect,
            on_disconnect=on_disconnect,
        )

    # --- Message parsing ---

    @staticmethod
    def _parse_agent_message(
        data: dict[str, Any],
    ) -> Transcription | SpeechRequest:
        """Parse an SSE message based on its type field."""
        msg_type = data.get("type")
        if msg_type == "speech":
            return SpeechRequest.from_dict(data)
        return Transcription.from_dict(data)

    # --- SSE helper ---

    def _sse_stream(
        self,
        url: str,
        parse: Callable[[dict[str, Any]], Any],
        *,
        reconnect: bool = False,
        retry_delay: float = 0.5,
        max_retry_delay: float = 5.0,
        stop: Callable[[], bool] | None = None,
        on_connect: Callable[[], None] | None = None,
        on_disconnect: Callable[[Exception | None], None] | None = None,
        conflict_message: str | None = None,
    ) -> Iterator[Any]:
        """Generic SSE stream consumer with reconnection support.

        Args:
            url: Full URL of the SSE endpoint.
            parse: Callable that converts a parsed JSON dict into the desired type.
            reconnect: Auto-reconnect on connection loss.
            retry_delay: Initial reconnection delay in seconds.
            max_retry_delay: Maximum reconnection delay.
            stop: Callable returning True to stop iteration.
            on_connect: Callback on successful connection.
            on_disconnect: Callback on disconnection with exception or None.
            conflict_message: Custom message for DuplicateAgentError (409).

        Yields:
            Parsed objects from the SSE stream.
        """
        current_delay = retry_delay

        while True:
            try:
                headers = {"Accept": "text/event-stream"}
                if self._token:
                    headers["Authorization"] = f"Bearer {self._token}"
                req = urllib.request.Request(url, headers=headers)
                with urllib.request.urlopen(req, timeout=None) as resp:
                    current_delay = retry_delay  # Reset on success
                    logger.debug("SSE connected: %s", url)
                    if on_connect:
                        on_connect()

                    for line in resp:
                        if stop and stop():
                            return
                        line = line.decode("utf-8").strip()
                        if line.startswith("data: "):
                            payload = line[6:]
                            try:
                                data = json.loads(payload)
                                yield parse(data)
                            except json.JSONDecodeError:
                                continue
                            except Exception:
                                logger.debug(
                                    "SSE parse error for %s: %s",
                                    payload[:200], __import__("traceback").format_exc(),
                                )
                                continue

                # Stream ended cleanly
                if on_disconnect:
                    on_disconnect(None)
                if not reconnect:
                    return

            except urllib.error.HTTPError as e:
                if e.code == 409:
                    msg = conflict_message or f"SSE conflict (409) for {url}"
                    raise DuplicateAgentError(msg) from e
                logger.warning("SSE HTTP %d for %s", e.code, url)
                if on_disconnect:
                    on_disconnect(e)
                if not reconnect:
                    raise

            except (ConnectionRefusedError, urllib.error.URLError, OSError) as e:
                logger.debug("SSE connection error for %s: %s", url, e)
                if on_disconnect:
                    on_disconnect(e)
                if not reconnect:
                    raise

            except Exception as e:
                logger.warning("SSE unexpected error for %s: %s", url, e)
                if on_disconnect:
                    on_disconnect(e)
                if not reconnect:
                    raise

            # Reconnect with backoff
            if stop and stop():
                return
            logger.debug("SSE reconnecting in %.1fs...", current_delay)
            time.sleep(current_delay)
            current_delay = min(current_delay * 2, max_retry_delay)

    # --- Internal HTTP helpers ---

    def _get(self, path: str) -> dict[str, Any]:
        """GET request."""
        req = urllib.request.Request(f"{self.url}{path}")
        if self._token:
            req.add_header("Authorization", f"Bearer {self._token}")
        with urllib.request.urlopen(req, timeout=self.timeout) as resp:
            return json.loads(resp.read())

    def _post(self, path: str, body: dict[str, Any]) -> dict[str, Any]:
        """POST request."""
        payload = json.dumps(body, default=str).encode()
        headers = {"Content-Type": "application/json"}
        if self._token:
            headers["Authorization"] = f"Bearer {self._token}"
        req = urllib.request.Request(
            f"{self.url}{path}",
            data=payload,
            headers=headers,
        )
        with urllib.request.urlopen(req, timeout=self.timeout) as resp:
            return json.loads(resp.read())
