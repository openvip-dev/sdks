"""Tests for hand-written message factories."""

from datetime import datetime, timezone
from uuid import UUID, uuid4

from openvip.messages import PROTOCOL_VERSION, create_speech_request, create_transcription


class TestCreateTranscription:
    def test_basic(self):
        msg = create_transcription("hello world")
        assert msg.text == "hello world"
        assert msg.openvip == PROTOCOL_VERSION
        assert msg.type == "transcription"

    def test_auto_id(self):
        msg = create_transcription("test")
        assert isinstance(msg.id, UUID)

    def test_unique_ids(self):
        a = create_transcription("a")
        b = create_transcription("b")
        assert a.id != b.id

    def test_auto_timestamp(self):
        before = datetime.now(timezone.utc)
        msg = create_transcription("test")
        after = datetime.now(timezone.utc)
        assert before <= msg.timestamp <= after

    def test_language(self):
        msg = create_transcription("ciao", language="it")
        assert msg.language == "it"

    def test_confidence(self):
        msg = create_transcription("test", confidence=0.95)
        assert msg.confidence == 0.95

    def test_partial(self):
        msg = create_transcription("hel", partial=True)
        assert msg.partial is True

    def test_origin(self):
        msg = create_transcription("test", origin="myapp/1.0.0")
        assert msg.origin == "myapp/1.0.0"

    def test_trace_ids(self):
        tid = uuid4()
        pid = uuid4()
        msg = create_transcription("test", trace_id=tid, parent_id=pid)
        assert msg.trace_id == tid
        assert msg.parent_id == pid

    def test_defaults_none(self):
        msg = create_transcription("test")
        assert msg.language is None
        assert msg.confidence is None
        assert msg.partial is None
        assert msg.origin is None
        assert msg.trace_id is None
        assert msg.parent_id is None

    def test_to_dict_roundtrip(self):
        msg = create_transcription("hello", language="en", confidence=0.9)
        d = msg.to_dict()
        assert d["text"] == "hello"
        assert d["openvip"] == PROTOCOL_VERSION
        assert d["type"] == "transcription"
        assert d["language"] == "en"
        assert d["confidence"] == 0.9
        assert "id" in d
        assert "timestamp" in d


class TestCreateSpeechRequest:
    def test_basic(self):
        req = create_speech_request("hello world")
        assert req.text == "hello world"
        assert req.openvip == PROTOCOL_VERSION
        assert req.type == "speech"

    def test_language(self):
        req = create_speech_request("ciao", language="it")
        assert req.language == "it"

    def test_no_language(self):
        req = create_speech_request("test")
        assert req.language is None

    def test_voice(self):
        req = create_speech_request("hello", voice="af_sky")
        assert req.voice == "af_sky"

    def test_no_voice(self):
        req = create_speech_request("test")
        assert req.voice is None

    def test_to_dict(self):
        req = create_speech_request("hello", language="en", voice="af_sky")
        d = req.to_dict()
        assert d["openvip"] == PROTOCOL_VERSION
        assert d["type"] == "speech"
        assert d["text"] == "hello"
        assert d["language"] == "en"
        assert d["voice"] == "af_sky"
        assert "id" in d
        assert "timestamp" in d
