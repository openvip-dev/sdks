// OpenVIP .NET SDK demo.
//
// Connects to a local OpenVIP engine (e.g. VoxType) and demonstrates
// SDK features: status, control, speech, and messaging.
//
// Usage:
//   dotnet run

using OpenVip.Api;
using OpenVip.Client;
using OpenVip.Model;

var baseUrl = args.Length > 0 ? args[0] : "http://localhost:8770";

Console.WriteLine("OpenVIP .NET SDK demo");
Console.WriteLine($"Connecting to {baseUrl}...");
Console.WriteLine();

// 1. Status
Console.WriteLine("=== GET /status ===");
try
{
    var statusApi = new StatusApi(baseUrl);
    var status = await statusApi.GetStatusAsync();
    Console.WriteLine($"  Protocol: {status.ProtocolVersion}");
    Console.WriteLine($"  Agents:   [{string.Join(", ", status.ConnectedAgents ?? new List<string>())}]");
}
catch (Exception e)
{
    Console.WriteLine($"  Error: {e.Message}");
    Console.WriteLine("  Is the engine running? Start VoxType with: voxtype listen --agents");
    Environment.Exit(1);
}
Console.WriteLine();

// 2. Control — start listening
Console.WriteLine("=== POST /control (stt.start) ===");
try
{
    var controlApi = new ControlApi(baseUrl);
    var ack = await controlApi.SendControlAsync(new ControlRequest(ControlRequest.CommandEnum.SttStart));
    Console.WriteLine($"  Response: {ack.Status}");
}
catch (Exception e)
{
    Console.WriteLine($"  Error: {e.Message}");
}
Console.WriteLine();

// 3. Speech
Console.WriteLine("=== POST /speech ===");
try
{
    var speechApi = new SpeechApi(baseUrl);
    var resp = await speechApi.TextToSpeechAsync(
        new SpeechRequest("1.0", SpeechRequest.TypeEnum.Speech, "Hello from the OpenVIP .NET SDK!")
        { Language = "en" }
    );
    Console.WriteLine($"  Status:   {resp.Status}");
    Console.WriteLine($"  Duration: {resp.DurationMs}ms");
}
catch (Exception e)
{
    Console.WriteLine($"  Error: {e.Message}");
}
Console.WriteLine();

// 4. Send message
Console.WriteLine("=== POST /agents/demo/messages ===");
try
{
    var messagesApi = new MessagesApi(baseUrl);
    var msg = new Transcription(
        openvip: "1.0",
        type: Transcription.TypeEnum.Transcription,
        id: Guid.NewGuid(),
        timestamp: DateTime.UtcNow,
        text: "Test message from .NET SDK demo"
    ) { Language = "en" };
    var ack = await messagesApi.SendMessageAsync("demo", msg);
    Console.WriteLine($"  Response: {ack.Status}");
}
catch (Exception e)
{
    Console.WriteLine($"  Error: {e.Message} (expected if no 'demo' agent connected)");
}
Console.WriteLine();

// 5. Control — stop listening
Console.WriteLine("=== POST /control (stt.stop) ===");
try
{
    var controlApi = new ControlApi(baseUrl);
    var ack = await controlApi.SendControlAsync(new ControlRequest(ControlRequest.CommandEnum.SttStop));
    Console.WriteLine($"  Response: {ack.Status}");
}
catch (Exception e)
{
    Console.WriteLine($"  Error: {e.Message}");
}
Console.WriteLine();

Console.WriteLine("Demo complete!");
