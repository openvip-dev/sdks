"""Tests for hand-written Client wrapper."""

import json
import urllib.error
from unittest.mock import MagicMock, call, patch

import pytest

from openvip import Client, DuplicateAgentError
from openvip.messages import PROTOCOL_VERSION, create_transcription
from openvip.models.ack import Ack
from openvip.models.speech_response import SpeechResponse
from openvip.models.status import Status


def _mock_response(data: dict) -> MagicMock:
    """Create a mock urllib response with JSON body."""
    resp = MagicMock()
    resp.read.return_value = json.dumps(data).encode()
    resp.__enter__ = lambda s: s
    resp.__exit__ = MagicMock(return_value=False)
    return resp


class TestClientInit:
    def test_default_url(self):
        c = Client()
        assert c.url == "http://localhost:8770"

    def test_custom_url(self):
        c = Client("http://myhost:9999")
        assert c.url == "http://myhost:9999"

    def test_strips_trailing_slash(self):
        c = Client("http://myhost:9999/")
        assert c.url == "http://myhost:9999"

    def test_custom_timeout(self):
        c = Client(timeout=30.0)
        assert c.timeout == 30.0


class TestClientSpeak:
    @patch("openvip.client.urllib.request.urlopen")
    def test_speak_basic(self, mock_urlopen):
        mock_urlopen.return_value = _mock_response({"openvip": "1.0", "status": "ok", "duration_ms": 1500})
        client = Client("http://test:8770")

        result = client.speak("hello", language="en")

        assert isinstance(result, SpeechResponse)
        assert result.status == "ok"
        assert result.duration_ms == 1500

        # Verify request
        call_args = mock_urlopen.call_args
        req = call_args[0][0]
        body = json.loads(req.data)
        assert body["text"] == "hello"
        assert body["language"] == "en"
        assert body["openvip"] == PROTOCOL_VERSION
        assert body["type"] == "speech"
        assert req.full_url == "http://test:8770/speech"

    @patch("openvip.client.urllib.request.urlopen")
    def test_speak_kwargs_passthrough(self, mock_urlopen):
        mock_urlopen.return_value = _mock_response({"openvip": "1.0", "status": "ok"})
        client = Client("http://test:8770")

        client.speak("hello", engine="espeak", voice="en-us", speed=180)

        body = json.loads(mock_urlopen.call_args[0][0].data)
        assert body["engine"] == "espeak"
        assert body["voice"] == "en-us"
        assert body["speed"] == 180

    @patch("openvip.client.urllib.request.urlopen")
    def test_speak_no_kwargs(self, mock_urlopen):
        mock_urlopen.return_value = _mock_response({"openvip": "1.0", "status": "ok"})
        client = Client("http://test:8770")

        client.speak("hello")

        body = json.loads(mock_urlopen.call_args[0][0].data)
        assert "engine" not in body
        assert "voice" not in body


class TestClientGetStatus:
    @patch("openvip.client.urllib.request.urlopen")
    def test_get_status(self, mock_urlopen):
        mock_urlopen.return_value = _mock_response({
            "openvip": "1.0",
            "connected_agents": ["claude", "shell"],
            "platform": {"state": "listening"},
        })
        client = Client("http://test:8770")

        status = client.get_status()

        assert isinstance(status, Status)
        assert status.openvip == "1.0"
        assert status.connected_agents == ["claude", "shell"]
        assert status.platform == {"state": "listening"}

        req = mock_urlopen.call_args[0][0]
        assert req.full_url == "http://test:8770/status"


class TestClientControl:
    @patch("openvip.client.urllib.request.urlopen")
    def test_control(self, mock_urlopen):
        mock_urlopen.return_value = _mock_response({"status": "ok"})
        client = Client("http://test:8770")

        result = client.control("stt.toggle")

        assert isinstance(result, Ack)
        assert result.status == "ok"

        body = json.loads(mock_urlopen.call_args[0][0].data)
        assert body == {"command": "stt.toggle"}
        assert mock_urlopen.call_args[0][0].full_url == "http://test:8770/control"

    @patch("openvip.client.urllib.request.urlopen")
    def test_start_listening(self, mock_urlopen):
        mock_urlopen.return_value = _mock_response({"status": "ok"})
        client = Client("http://test:8770")

        client.start_listening()

        body = json.loads(mock_urlopen.call_args[0][0].data)
        assert body == {"command": "stt.start"}

    @patch("openvip.client.urllib.request.urlopen")
    def test_stop_listening(self, mock_urlopen):
        mock_urlopen.return_value = _mock_response({"status": "ok"})
        client = Client("http://test:8770")

        client.stop_listening()

        body = json.loads(mock_urlopen.call_args[0][0].data)
        assert body == {"command": "stt.stop"}

    @patch("openvip.client.urllib.request.urlopen")
    def test_shutdown(self, mock_urlopen):
        mock_urlopen.return_value = _mock_response({"status": "ok"})
        client = Client("http://test:8770")

        client.shutdown()

        body = json.loads(mock_urlopen.call_args[0][0].data)
        assert body == {"command": "engine.shutdown"}


class TestClientSendMessage:
    @patch("openvip.client.urllib.request.urlopen")
    def test_send_message(self, mock_urlopen):
        mock_urlopen.return_value = _mock_response({"status": "ok"})
        client = Client("http://test:8770")

        msg = create_transcription("turn on the light", language="en")
        result = client.send_message("my-agent", msg)

        assert isinstance(result, Ack)
        req = mock_urlopen.call_args[0][0]
        assert req.full_url == "http://test:8770/agents/my-agent/messages"

        body = json.loads(req.data)
        assert body["text"] == "turn on the light"
        assert body["openvip"] == PROTOCOL_VERSION


class _FakeSSEResponse:
    """Fake HTTP response that yields lines like a real SSE stream."""

    def __init__(self, lines: list[bytes]) -> None:
        self._lines = lines

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False

    def __iter__(self):
        return iter(self._lines)


class TestClientSubscribe:
    @patch("openvip.client.urllib.request.urlopen")
    def test_subscribe_yields_transcriptions(self, mock_urlopen):
        id1 = "550e8400-e29b-41d4-a716-446655440000"
        id2 = "6ba7b810-9dad-11d1-80b4-00c04fd430c8"
        lines = [
            b"event: transcription\n",
            f'data: {{"openvip":"1.0","type":"transcription","id":"{id1}","timestamp":"2026-01-01T00:00:00Z","text":"hello"}}\n'.encode(),
            b"\n",
            f'data: {{"openvip":"1.0","type":"transcription","id":"{id2}","timestamp":"2026-01-01T00:00:01Z","text":"world"}}\n'.encode(),
            b"\n",
        ]
        mock_urlopen.return_value = _FakeSSEResponse(lines)

        client = Client("http://test:8770")
        messages = list(client.subscribe("my-agent"))

        assert len(messages) == 2
        assert messages[0].text == "hello"
        assert messages[1].text == "world"

        req = mock_urlopen.call_args[0][0]
        assert req.full_url == "http://test:8770/agents/my-agent/messages"
        assert req.headers["Accept"] == "text/event-stream"

    @patch("openvip.client.urllib.request.urlopen")
    def test_subscribe_skips_bad_json(self, mock_urlopen):
        valid_id = "550e8400-e29b-41d4-a716-446655440000"
        lines = [
            b"data: not-json\n",
            f'data: {{"openvip":"1.0","type":"transcription","id":"{valid_id}","timestamp":"2026-01-01T00:00:00Z","text":"ok"}}\n'.encode(),
        ]
        mock_urlopen.return_value = _FakeSSEResponse(lines)

        client = Client("http://test:8770")
        messages = list(client.subscribe("my-agent"))

        assert len(messages) == 1
        assert messages[0].text == "ok"

    @patch("openvip.client.urllib.request.urlopen")
    def test_subscribe_raises_duplicate_agent_on_409(self, mock_urlopen):
        mock_urlopen.side_effect = urllib.error.HTTPError(
            url="http://test:8770/agents/my-agent/messages",
            code=409,
            msg="Conflict",
            hdrs=None,
            fp=None,
        )
        client = Client("http://test:8770")

        with pytest.raises(DuplicateAgentError, match="already connected"):
            list(client.subscribe("my-agent"))

    @patch("openvip.client.urllib.request.urlopen")
    def test_subscribe_calls_on_connect(self, mock_urlopen):
        valid_id = "550e8400-e29b-41d4-a716-446655440000"
        lines = [
            f'data: {{"openvip":"1.0","type":"transcription","id":"{valid_id}","timestamp":"2026-01-01T00:00:00Z","text":"hi"}}\n'.encode(),
        ]
        mock_urlopen.return_value = _FakeSSEResponse(lines)

        callback = MagicMock()
        client = Client("http://test:8770")
        list(client.subscribe("my-agent", on_connect=callback))

        callback.assert_called_once()

    @patch("openvip.client.urllib.request.urlopen")
    def test_subscribe_calls_on_disconnect(self, mock_urlopen):
        mock_urlopen.return_value = _FakeSSEResponse([])  # Empty stream

        callback = MagicMock()
        client = Client("http://test:8770")
        list(client.subscribe("my-agent", on_disconnect=callback))

        callback.assert_called_once_with(None)

    @patch("openvip.client.time.sleep")
    @patch("openvip.client.urllib.request.urlopen")
    def test_subscribe_reconnect_on_connection_error(self, mock_urlopen, mock_sleep):
        valid_id = "550e8400-e29b-41d4-a716-446655440000"
        lines = [
            f'data: {{"openvip":"1.0","type":"transcription","id":"{valid_id}","timestamp":"2026-01-01T00:00:00Z","text":"recovered"}}\n'.encode(),
        ]
        # First call fails, second succeeds
        mock_urlopen.side_effect = [
            ConnectionRefusedError("refused"),
            _FakeSSEResponse(lines),
        ]
        got_message = False

        def stop_after_message():
            return got_message

        client = Client("http://test:8770")
        messages = []
        for msg in client.subscribe("my-agent", reconnect=True, stop=stop_after_message):
            messages.append(msg)
            got_message = True

        assert len(messages) == 1
        assert messages[0].text == "recovered"
        mock_sleep.assert_called_once_with(0.5)

    @patch("openvip.client.time.sleep")
    @patch("openvip.client.urllib.request.urlopen")
    def test_subscribe_reconnect_exponential_backoff(self, mock_urlopen, mock_sleep):
        valid_id = "550e8400-e29b-41d4-a716-446655440000"
        lines = [
            f'data: {{"openvip":"1.0","type":"transcription","id":"{valid_id}","timestamp":"2026-01-01T00:00:00Z","text":"ok"}}\n'.encode(),
        ]
        # Three failures then success
        mock_urlopen.side_effect = [
            ConnectionRefusedError("refused"),
            ConnectionRefusedError("refused"),
            ConnectionRefusedError("refused"),
            _FakeSSEResponse(lines),
        ]
        got_message = False

        def stop_after_message():
            return got_message

        client = Client("http://test:8770")
        for msg in client.subscribe("my-agent", reconnect=True, stop=stop_after_message):
            got_message = True

        assert mock_sleep.call_args_list == [call(0.5), call(1.0), call(2.0)]

    @patch("openvip.client.time.sleep")
    @patch("openvip.client.urllib.request.urlopen")
    def test_subscribe_reconnect_max_delay(self, mock_urlopen, mock_sleep):
        valid_id = "550e8400-e29b-41d4-a716-446655440000"
        lines = [
            f'data: {{"openvip":"1.0","type":"transcription","id":"{valid_id}","timestamp":"2026-01-01T00:00:00Z","text":"ok"}}\n'.encode(),
        ]
        # Many failures to hit max delay
        mock_urlopen.side_effect = [
            ConnectionRefusedError("refused"),
            ConnectionRefusedError("refused"),
            ConnectionRefusedError("refused"),
            ConnectionRefusedError("refused"),
            ConnectionRefusedError("refused"),
            _FakeSSEResponse(lines),
        ]
        got_message = False

        def stop_after_message():
            return got_message

        client = Client("http://test:8770")
        for msg in client.subscribe("my-agent", reconnect=True, max_retry_delay=2.0, stop=stop_after_message):
            got_message = True

        # 0.5, 1.0, 2.0, 2.0, 2.0 (capped at max)
        delays = [c.args[0] for c in mock_sleep.call_args_list]
        assert delays == [0.5, 1.0, 2.0, 2.0, 2.0]

    @patch("openvip.client.urllib.request.urlopen")
    def test_subscribe_reconnect_still_raises_on_409(self, mock_urlopen):
        mock_urlopen.side_effect = urllib.error.HTTPError(
            url="", code=409, msg="Conflict", hdrs=None, fp=None,
        )
        client = Client("http://test:8770")

        with pytest.raises(DuplicateAgentError):
            list(client.subscribe("my-agent", reconnect=True))

    @patch("openvip.client.urllib.request.urlopen")
    def test_subscribe_stop_callable(self, mock_urlopen):
        valid_id = "550e8400-e29b-41d4-a716-446655440000"
        call_count = 0

        def stop():
            nonlocal call_count
            call_count += 1
            return call_count > 2

        lines = [
            f'data: {{"openvip":"1.0","type":"transcription","id":"{valid_id}","timestamp":"2026-01-01T00:00:00Z","text":"a"}}\n'.encode(),
            f'data: {{"openvip":"1.0","type":"transcription","id":"{valid_id}","timestamp":"2026-01-01T00:00:01Z","text":"b"}}\n'.encode(),
            f'data: {{"openvip":"1.0","type":"transcription","id":"{valid_id}","timestamp":"2026-01-01T00:00:02Z","text":"c"}}\n'.encode(),
        ]
        mock_urlopen.return_value = _FakeSSEResponse(lines)

        client = Client("http://test:8770")
        messages = list(client.subscribe("my-agent", stop=stop))

        assert len(messages) == 2

    @patch("openvip.client.urllib.request.urlopen")
    def test_subscribe_no_reconnect_raises_on_error(self, mock_urlopen):
        mock_urlopen.side_effect = ConnectionRefusedError("refused")
        client = Client("http://test:8770")

        with pytest.raises(ConnectionRefusedError):
            list(client.subscribe("my-agent", reconnect=False))


class TestClientIsAvailable:
    @patch("openvip.client.urllib.request.urlopen")
    def test_is_available_true(self, mock_urlopen):
        mock_urlopen.return_value = _mock_response({
            "openvip": "1.0",
            "connected_agents": [],
        })
        client = Client("http://test:8770")

        assert client.is_available() is True

    @patch("openvip.client.urllib.request.urlopen")
    def test_is_available_false(self, mock_urlopen):
        mock_urlopen.side_effect = ConnectionRefusedError("refused")
        client = Client("http://test:8770")

        assert client.is_available() is False
