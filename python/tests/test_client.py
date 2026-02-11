"""Tests for hand-written Client wrapper."""

import json
from unittest.mock import MagicMock, patch

from openvip import Client
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
        mock_urlopen.return_value = _mock_response({"status": "ok", "duration_ms": 1500})
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
        mock_urlopen.return_value = _mock_response({"status": "ok"})
        client = Client("http://test:8770")

        client.speak("hello", engine="espeak", voice="en-us", speed=180)

        body = json.loads(mock_urlopen.call_args[0][0].data)
        assert body["engine"] == "espeak"
        assert body["voice"] == "en-us"
        assert body["speed"] == 180

    @patch("openvip.client.urllib.request.urlopen")
    def test_speak_no_kwargs(self, mock_urlopen):
        mock_urlopen.return_value = _mock_response({"status": "ok"})
        client = Client("http://test:8770")

        client.speak("hello")

        body = json.loads(mock_urlopen.call_args[0][0].data)
        assert "engine" not in body
        assert "voice" not in body


class TestClientGetStatus:
    @patch("openvip.client.urllib.request.urlopen")
    def test_get_status(self, mock_urlopen):
        mock_urlopen.return_value = _mock_response({
            "protocol_version": "1.0",
            "connected_agents": ["claude", "shell"],
            "platform": {"state": "listening"},
        })
        client = Client("http://test:8770")

        status = client.get_status()

        assert isinstance(status, Status)
        assert status.protocol_version == "1.0"
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
