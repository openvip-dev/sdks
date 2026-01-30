# OpenVIP SDKs

Auto-generated client SDKs for the [OpenVIP Protocol](https://github.com/open-voice-input/spec).

## Quick Start

### Python

```bash
pip install openvip
```

```python
from openvip import AgentsApi, Message

api = AgentsApi()
api.send_message("agent-uuid", Message(
    openvip="1.0",
    type="message",
    text="Turn on the lights"
))
```

### .NET

```bash
dotnet add package OpenVip
```

```csharp
using OpenVip.Api;
using OpenVip.Model;

var api = new AgentsApi();
api.SendMessage("agent-uuid", new Message(
    openvip: "1.0",
    type: MessageType.Message,
    text: "Turn on the lights"
));
```

## Available SDKs

| Language | Package | Status |
|----------|---------|--------|
| Python | `openvip` | ✅ Generated |
| .NET | `OpenVip` | ✅ Generated |
| TypeScript | `openvip` | 🔜 Planned |
| Go | `openvip` | 🔜 Planned |
| Rust | `openvip` | 🔜 Planned |
| Swift | `OpenVip` | 🔜 Planned |
| Kotlin | `org.openvip` | 🔜 Planned |
| Java | `org.openvip` | 🔜 Planned |

## Generating SDKs

Requires [Docker](https://www.docker.com/).

### From spec URL (recommended)

```bash
./generate.sh https://raw.githubusercontent.com/open-voice-input/spec/main/bindings/http/openapi.yaml
```

### From local file

```bash
./generate.sh /path/to/openapi.yaml
```

### Generate specific language only

```bash
./generate.sh https://... --only python
./generate.sh https://... --only dotnet
```

## SDK Structure

```
openvip-sdks/
├── python/          # Python SDK
│   ├── openvip/
│   ├── setup.py
│   └── README.md
├── dotnet/          # .NET SDK
│   ├── src/
│   └── OpenVip.sln
└── generate.sh      # Generation script
```

## Versioning

SDKs follow [Semantic Versioning](https://semver.org/). SDK versions may differ from the protocol version.

| Protocol | SDK |
|----------|-----|
| v1.0 | 1.0.x |
| v1.1 | 1.1.x |

## Contributing

1. Update the OpenAPI spec in the [spec repo](https://github.com/open-voice-input/spec)
2. Run `./generate.sh` to regenerate SDKs
3. Test the changes
4. Submit a PR

## License

Apache 2.0 - See [LICENSE](LICENSE) for details.
