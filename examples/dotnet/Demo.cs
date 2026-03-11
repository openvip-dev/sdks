// OpenVIP .NET SDK demo
// Usage: dotnet run [NAME]

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
    await foreach (var status in client.SubscribeStatusAsync(
        new SubscribeOptions { Reconnect = true }, cts.Token))
    {
        // Note: platform dict access not yet available in StatusDto
        Console.WriteLine("[agent] Hey, I'm here!");
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
            await client.SpeakAsync($"You said: {message.Text}", language: "en", ct: cts.Token);
    }
}
catch (OperationCanceledException) { }

Console.WriteLine("\nStopped.");
