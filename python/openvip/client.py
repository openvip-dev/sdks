"""High-level OpenVIP client."""

from __future__ import annotations

import json
import urllib.error
import urllib.request
from typing import Any, Iterator

from openvip.messages import PROTOCOL_VERSION, create_speech_request
from openvip.models.ack import Ack
from openvip.models.speech_response import SpeechResponse
from openvip.models.status import Status
from openvip.models.transcription import Transcription

DEFAULT_URL = "http://localhost:8770"


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

    def __init__(self, url: str = DEFAULT_URL, *, timeout: float = 10.0) -> None:
        """Initialize client.

        Args:
            url: Base URL of the OpenVIP engine (default: http://localhost:8770).
            timeout: HTTP request timeout in seconds.
        """
        self.url = url.rstrip("/")
        self.timeout = timeout

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

    def subscribe(self, agent_id: str) -> Iterator[Transcription]:
        """Subscribe to messages for an agent via SSE.

        This is a blocking iterator that yields messages as they arrive.
        The SSE connection acts as agent registration — the agent exists
        as long as this iterator is active.

        Args:
            agent_id: Agent identifier to register.

        Yields:
            Transcription messages from the engine.
        """
        url = f"{self.url}/agents/{agent_id}/messages"
        req = urllib.request.Request(url, headers={"Accept": "text/event-stream"})

        with urllib.request.urlopen(req, timeout=None) as resp:
            for line in resp:
                line = line.decode("utf-8").strip()
                if line.startswith("data: "):
                    payload = line[6:]
                    try:
                        data = json.loads(payload)
                        yield Transcription.from_dict(data)
                    except (json.JSONDecodeError, Exception):
                        continue

    # --- Internal HTTP helpers ---

    def _get(self, path: str) -> dict[str, Any]:
        """GET request."""
        req = urllib.request.Request(f"{self.url}{path}")
        with urllib.request.urlopen(req, timeout=self.timeout) as resp:
            return json.loads(resp.read())

    def _post(self, path: str, body: dict[str, Any]) -> dict[str, Any]:
        """POST request."""
        payload = json.dumps(body, default=str).encode()
        req = urllib.request.Request(
            f"{self.url}{path}",
            data=payload,
            headers={"Content-Type": "application/json"},
        )
        with urllib.request.urlopen(req, timeout=self.timeout) as resp:
            return json.loads(resp.read())
