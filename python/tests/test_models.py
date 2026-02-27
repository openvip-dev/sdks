"""Tests for generated Pydantic models.

Regression guard: if the SDK is regenerated without the post-processing
patch (patch_pydantic_models.py), these tests fail immediately because
unknown/extension fields (like x_input) would be silently dropped.
"""

from datetime import datetime, timezone
from uuid import uuid4

import pytest

from openvip.models import Transcription, SpeechRequest, Response


# ---------------------------------------------------------------------------
# Fixtures — minimal valid dicts for each model
# ---------------------------------------------------------------------------

def _transcription_dict(**extra):
    d = {
        "openvip": "1.0",
        "type": "transcription",
        "id": str(uuid4()),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "text": "hello",
    }
    d.update(extra)
    return d


def _speech_request_dict(**extra):
    d = {
        "openvip": "1.0",
        "type": "speech",
        "id": str(uuid4()),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "text": "hello",
    }
    d.update(extra)
    return d


def _response_dict(**extra):
    d = {
        "openvip": "1.0",
        "status": "ok",
    }
    d.update(extra)
    return d


# ---------------------------------------------------------------------------
# Extension fields survive from_dict → to_dict round-trip
# ---------------------------------------------------------------------------

class TestExtensionFieldsRoundTrip:
    """Verify that unknown fields (x_input, x_flags, etc.) are preserved.

    OpenAPI schemas allow additional properties by default.  The generated
    Pydantic models must honour this — extra fields must not be dropped.
    """

    def test_transcription_x_input_newline(self):
        data = _transcription_dict(x_input={"newline": True})
        t = Transcription.from_dict(data)
        assert t.x_input == {"newline": True}
        assert t.to_dict()["x_input"] == {"newline": True}

    def test_transcription_x_input_submit(self):
        data = _transcription_dict(x_input={"submit": True})
        t = Transcription.from_dict(data)
        assert t.x_input == {"submit": True}
        assert t.to_dict()["x_input"] == {"submit": True}

    def test_speech_request_extra_field(self):
        data = _speech_request_dict(x_custom={"key": "value"})
        s = SpeechRequest.from_dict(data)
        assert s.x_custom == {"key": "value"}
        assert s.to_dict()["x_custom"] == {"key": "value"}

    def test_response_extra_field(self):
        data = _response_dict(x_meta={"engine": "kokoro"})
        r = Response.from_dict(data)
        assert r.x_meta == {"engine": "kokoro"}
        assert r.to_dict()["x_meta"] == {"engine": "kokoro"}

    def test_multiple_extra_fields(self):
        data = _transcription_dict(
            x_input={"newline": True},
            x_flags={"urgent": True},
        )
        t = Transcription.from_dict(data)
        assert t.x_input == {"newline": True}
        assert t.x_flags == {"urgent": True}
        d = t.to_dict()
        assert d["x_input"] == {"newline": True}
        assert d["x_flags"] == {"urgent": True}

    def test_scalar_extra_field(self):
        data = _transcription_dict(x_version=42)
        t = Transcription.from_dict(data)
        assert t.x_version == 42

    def test_known_fields_still_work(self):
        """Sanity check: known fields are not broken by extra='allow'."""
        data = _transcription_dict(language="it", confidence=0.95)
        t = Transcription.from_dict(data)
        assert t.text == "hello"
        assert t.language == "it"
        assert t.confidence == 0.95
        assert t.openvip == "1.0"


# ---------------------------------------------------------------------------
# model_validate preserves extras (constructor path)
# ---------------------------------------------------------------------------

class TestModelValidateExtras:
    """Verify extra fields work via model_validate (not just from_dict)."""

    def test_transcription_model_validate(self):
        data = _transcription_dict(x_input={"submit": True})
        t = Transcription.model_validate(data)
        assert t.x_input == {"submit": True}

    def test_speech_request_model_validate(self):
        data = _speech_request_dict(x_priority="high")
        s = SpeechRequest.model_validate(data)
        assert s.x_priority == "high"
