# Changelog

## [1.0.0rc4] - 2026-02-26

### Added
- `SpeechRequest` now includes `voice` field (optional, engine-specific voice
  identifier, e.g. `"af_sky"` for Kokoro). Spec updated in `openapi.yaml` and
  `openvip-1.0.md`; SDK regenerated.
- `create_speech_request()` accepts `voice` parameter.

## [1.0.0rc3] - 2026-02-26

### Fixed
- CI: added `actions/setup-dotnet@v4` (dotnet-version: 10.0.x) to .NET build
  job — self-hosted runner had .NET 9 but project targets net10.0

## [1.0.0rc2] - 2026-02-26

### Fixed
- `SpeechRequest` model now includes `id` (UUID) and `timestamp` fields, matching
  the OpenVIP v1.0 spec (`SpeechRequest` extends `Message` which requires them).
  Previously the model was generated from an older spec version that lacked them.
- `create_speech_request()` now auto-fills `id` and `timestamp`, consistent with
  `create_transcription()`.
- `generate.sh`: removed `rm -rf` before generation; rely on `.openapi-generator-ignore`
  to protect hand-written files during regeneration.
- `pyproject.toml` added to `.openapi-generator-ignore` to prevent it being overwritten.

## [1.0.0rc1] - 2026-02-24

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
- Logging via `logging.getLogger(__name__)`
