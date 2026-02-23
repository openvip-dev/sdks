# Changelog

## [1.0.1] - 2026-02-23

### Fixed
- `SSE HTTP 401` no longer logged at WARNING level; downgraded to DEBUG since
  401s are handled gracefully via the `on_disconnect` callback (token refresh).

## [1.0.0] - 2026-02-23

### Added
- High-level `Client` class with `speak()`, `get_status()`, `control()`, `send_message()`, `subscribe()`
- Message factories: `create_transcription()`, `create_speech_request()`
- Pydantic v2 models: `Transcription`, `SpeechRequest`, `SpeechResponse`, `Status`, `Ack`, `Error`
- Auto-generated low-level API from OpenAPI spec
- `subscribe()`: `reconnect` parameter with exponential backoff (0.5s → configurable max)
- `subscribe()`: `stop` callable to gracefully terminate the iterator
- `subscribe()`: `on_connect` / `on_disconnect` callbacks for connection lifecycle events
- `subscribe_status()`: SSE stream for engine status changes
- `DuplicateAgentError` exception for HTTP 409 (agent already connected)
- `Client.is_available()` health check method
- Bearer token authorization: `Client(url, token="...")` adds `Authorization` header to all requests
- Logging via `logging.getLogger(__name__)`
