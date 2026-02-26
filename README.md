# OpenVIP SDKs

Client SDKs for the [Open Voice Interaction Protocol](https://github.com/open-voice-input/open-voice-input).

Generated from the OpenAPI spec + hand-written convenience wrappers.

## Quick Start

### Python

```bash
pip install openvip
```

```python
from openvip import Client, create_transcription

client = Client()  # http://localhost:8770

# Text-to-speech
client.speak("Hello world", language="en")

# Get engine status
status = client.get_status()
print(status.connected_agents)

# Control
client.start_listening()
client.stop_listening()

# Create and send a message
msg = create_transcription("turn on the light", language="en")
client.send_message("my-agent", msg)

# Subscribe to messages (SSE)
for message in client.subscribe("my-agent"):
    print(message.text)
```

### TypeScript

```bash
npm install openvip
```

```typescript
import { StatusApi, ControlApi, SpeechApi, Configuration } from "openvip";

const config = new Configuration({ basePath: "http://localhost:8770" });

const status = await new StatusApi(config).getStatus();
console.log(status.connectedAgents);

await new ControlApi(config).sendControl({ command: "stt.start" });

await new SpeechApi(config).textToSpeech({
  openvip: "1.0", type: "speech",
  text: "Hello world", language: "en",
});
```

### Go

```go
import openapi "github.com/openvip/go"

config := openapi.NewConfiguration()
client := openapi.NewAPIClient(config)

status, _, _ := client.StatusAPI.GetStatus(ctx).Execute()
fmt.Println(status.ConnectedAgents)
```

### .NET

```bash
dotnet add package OpenVip
```

```csharp
using OpenVip.Api;
using OpenVip.Model;

var statusApi = new StatusApi("http://localhost:8770");
var status = await statusApi.GetStatusAsync();
Console.WriteLine(string.Join(", ", status.ConnectedAgents));
```

## Available SDKs

| Language | Package | Status |
|----------|---------|--------|
| Python | `openvip` | Generated + convenience wrapper |
| .NET | `OpenVip` | Generated |
| TypeScript | `openvip` | Generated |
| Go | `openvip` | Generated |
| Rust | `openvip` | Planned |
| Swift | `OpenVip` | Planned |
| Kotlin | `org.openvip` | Planned |
| Java | `org.openvip` | Planned |

## Examples

Each SDK has a runnable demo in `examples/`. Start an OpenVIP engine, then:

```bash
# Python
cd examples/python
pip install -e ../../python
python demo.py

# TypeScript
cd examples/typescript
npx ts-node demo.ts

# Go
cd examples/go
go run main.go

# .NET
cd examples/dotnet
dotnet run
```

The demos connect to `http://localhost:8770` (default) and exercise all protocol features: status, control, speech, messaging, and subscription.

## Generating SDKs

Requires [Docker](https://www.docker.com/).

```bash
# From spec URL (recommended)
./generate.sh

# From local file
./generate.sh /path/to/openapi.yaml

# Single language
./generate.sh --only python
```

Hand-written wrapper files (`client.py`, `messages.py`, `__init__.py`) are protected from regeneration via `.openapi-generator-ignore`.

## SDK Structure

```
openvip-sdks/
├── python/             # Python SDK
│   └── openvip/
│       ├── client.py       ← Hand-written: high-level Client
│       ├── messages.py     ← Hand-written: create_transcription(), etc.
│       ├── __init__.py     ← Hand-written: public API
│       ├── api/            ← Generated: low-level API
│       ├── models/         ← Generated: Pydantic models
│       └── ...             ← Generated: HTTP layer
├── typescript/         # TypeScript SDK (generated)
├── go/                 # Go SDK (generated)
├── dotnet/             # .NET SDK (generated)
├── examples/           # Runnable demos per language
│   ├── python/demo.py
│   ├── typescript/demo.ts
│   ├── go/main.go
│   └── dotnet/Demo.cs
└── generate.sh         # Generation script (Docker)
```

## Versioning

SDKs follow [Semantic Versioning](https://semver.org/). SDK versions may differ from the protocol version.

## Contributing

1. Update the OpenAPI spec in the [protocol repo](https://github.com/open-voice-input/open-voice-input)
2. Run `./generate.sh` to regenerate SDKs
3. Add/update wrapper code if needed
4. Test with `examples/`
5. Submit a PR

## License

Apache 2.0 — See [LICENSE](LICENSE) for details.
