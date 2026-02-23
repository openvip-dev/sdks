"""OpenVIP SDK — Open Voice Interaction Protocol client for Python.

Example::

    from openvip import Client, create_transcription

    # High-level client
    client = Client("http://localhost:8770")
    client.speak("Hello world", language="en")
    status = client.get_status()
    client.start_listening()

    # Message factories
    msg = create_transcription("turn on the light", language="en")
    client.send_message("my-agent", msg)

    # SSE subscription (agent messages)
    for message in client.subscribe("my-agent"):
        print(message.text)

    # SSE subscription (status changes)
    for status in client.subscribe_status(reconnect=True):
        print(status.state, status.connected_agents)
"""

__version__ = "1.1.0"

# Convenience API (hand-written)
from openvip.client import Client as Client
from openvip.client import DuplicateAgentError as DuplicateAgentError
from openvip.messages import (
    PROTOCOL_VERSION as PROTOCOL_VERSION,
    create_speech_request as create_speech_request,
    create_transcription as create_transcription,
)

# Generated models
from openvip.models.ack import Ack as Ack
from openvip.models.control_request import ControlRequest as ControlRequest
from openvip.models.error import Error as Error
from openvip.models.speech_request import SpeechRequest as SpeechRequest
from openvip.models.speech_response import SpeechResponse as SpeechResponse
from openvip.models.status import Status as Status
from openvip.models.transcription import Transcription as Transcription

# Generated low-level API (available if needed)
from openvip.api.control_api import ControlApi as ControlApi
from openvip.api.messages_api import MessagesApi as MessagesApi
from openvip.api.speech_api import SpeechApi as SpeechApi
from openvip.api.status_api import StatusApi as StatusApi
from openvip.api_client import ApiClient as ApiClient
from openvip.configuration import Configuration as Configuration

__all__ = [
    # Convenience (use these)
    "Client",
    "DuplicateAgentError",
    "create_transcription",
    "create_speech_request",
    "PROTOCOL_VERSION",
    # Models
    "Ack",
    "ControlRequest",
    "Error",
    "SpeechRequest",
    "SpeechResponse",
    "Status",
    "Transcription",
    # Low-level generated API
    "ControlApi",
    "MessagesApi",
    "SpeechApi",
    "StatusApi",
    "ApiClient",
    "Configuration",
]
