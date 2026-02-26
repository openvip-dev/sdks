"""Convenience factories for OpenVIP messages."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any
from uuid import uuid4

from openvip.models.speech_request import SpeechRequest
from openvip.models.transcription import Transcription

PROTOCOL_VERSION = "1.0"


def create_transcription(
    text: str,
    *,
    language: str | None = None,
    confidence: float | None = None,
    partial: bool | None = None,
    origin: str | None = None,
    trace_id: str | None = None,
    parent_id: str | None = None,
    **extensions: Any,
) -> Transcription:
    """Create a Transcription message with auto-filled protocol fields.

    Args:
        text: Transcribed text.
        language: BCP 47 language tag (e.g. "en", "it").
        confidence: Transcription confidence 0.0-1.0.
        partial: True if this is an incomplete transcription.
        origin: Producer identifier (e.g. "myapp/1.0.0").
        trace_id: ID of the original message (tracing).
        parent_id: ID of the parent message (tracing).
        **extensions: Additional x_ extension fields.

    Returns:
        Transcription with id, timestamp, and protocol version auto-filled.
    """
    msg = Transcription(
        openvip=PROTOCOL_VERSION,
        type="transcription",
        id=uuid4(),
        timestamp=datetime.now(timezone.utc),
        text=text,
        language=language,
        confidence=confidence,
        partial=partial,
        origin=origin,
        trace_id=trace_id,
        parent_id=parent_id,
    )
    # x_ extension fields go into additional_properties
    if extensions:
        msg.additional_properties = extensions
    return msg


def create_speech_request(
    text: str,
    *,
    language: str | None = None,
) -> SpeechRequest:
    """Create a SpeechRequest with auto-filled protocol fields.

    Args:
        text: Text to synthesize.
        language: BCP 47 language tag (e.g. "en", "it").

    Returns:
        SpeechRequest with protocol version auto-filled.
    """
    return SpeechRequest(
        openvip=PROTOCOL_VERSION,
        type="speech",
        id=uuid4(),
        timestamp=datetime.now(timezone.utc),
        text=text,
        language=language,
    )
