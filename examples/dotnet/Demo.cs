// OpenVIP .NET SDK demo
// Usage: dotnet run [NAME]

using System.Text.Json;
using OpenVip;

var name = args.Length > 0 ? args[0] : "demo";
var client = new OpenVipClient();

if (!await client.IsAvailableAsync())
{
    Console.WriteLine("Engine not available");
    return 1;
}

var cts = new CancellationTokenSource();
Console.CancelKeyPress += (_, e) => { e.Cancel = true; cts.Cancel(); };

// Watch which agent has focus and print a message when it changes
_ = Task.Run(async () =>
{
    bool? wasFocused = null;
    await foreach (var status in client.SubscribeStatusAsync(
        new SubscribeOptions { Reconnect = true }, cts.Token))
    {
        var isFocused = false;
        if (status.Platform != null
            && status.Platform.TryGetValue("output", out var output)
            && output.TryGetProperty("current_agent", out var agent))
        {
            isFocused = agent.GetString() == name;
        }

        if (isFocused != wasFocused)
        {
            wasFocused = isFocused;
            Console.WriteLine(isFocused ? "[agent] Hey, I'm here!" : "[agent] Ok, I'll wait here.");
        }
    }
});

// Listen for transcriptions and echo them back via TTS
try
{
    await foreach (var message in client.SubscribeAsync(name,
        new SubscribeOptions { Reconnect = true }, cts.Token))
    {
        Console.WriteLine($"[user ] {message.Text}");

        if (!string.IsNullOrWhiteSpace(message.Text))
        {
            try { await client.SpeakAsync($"You said: {message.Text}", language: "en", ct: cts.Token); }
            catch (HttpRequestException) { }
        }
    }
}
catch (OperationCanceledException) { }

Console.WriteLine("\nStopped.");
return 0;
