using System.Net;
using System.Net.Http;
using System.Text;
using System.Text.Json;
using OpenVip;
using Xunit;

namespace OpenVip.Test;

/// <summary>
/// Tests for the high-level OpenVipClient convenience wrapper.
/// Uses a mock HttpMessageHandler to avoid real HTTP calls.
/// </summary>
public class OpenVipClientTests
{
    private static readonly JsonSerializerOptions JsonOptions = new()
    {
        PropertyNamingPolicy = JsonNamingPolicy.SnakeCaseLower,
    };

    private static HttpClient MockHttp(HttpStatusCode status, object? body = null)
    {
        var json = body != null ? JsonSerializer.Serialize(body, JsonOptions) : "{}";
        var handler = new MockHandler(status, json);
        return new HttpClient(handler) { BaseAddress = new Uri("http://test:8770/openvip/") };
    }

    // --- GetStatusAsync ---

    [Fact]
    public async Task GetStatusAsync_ReturnsStatus()
    {
        var http = MockHttp(HttpStatusCode.OK, new
        {
            protocol_version = "1.0",
            connected_agents = new[] { "agent-1" },
        });
        using var client = new OpenVipClient(http);

        var status = await client.GetStatusAsync();

        Assert.Equal("1.0", status.ProtocolVersion);
        Assert.Single(status.ConnectedAgents!);
        Assert.Equal("agent-1", status.ConnectedAgents![0]);
    }

    // --- IsAvailableAsync ---

    [Fact]
    public async Task IsAvailableAsync_ReturnsTrueWhenReachable()
    {
        var http = MockHttp(HttpStatusCode.OK, new { protocol_version = "1.0" });
        using var client = new OpenVipClient(http);

        Assert.True(await client.IsAvailableAsync());
    }

    [Fact]
    public async Task IsAvailableAsync_ReturnsFalseOnError()
    {
        var handler = new MockHandler(new HttpRequestException("Connection refused"));
        var http = new HttpClient(handler) { BaseAddress = new Uri("http://test:8770/openvip/") };
        using var client = new OpenVipClient(http);

        Assert.False(await client.IsAvailableAsync());
    }

    // --- SpeakAsync ---

    [Fact]
    public async Task SpeakAsync_ReturnsSpeechResponse()
    {
        var http = MockHttp(HttpStatusCode.OK, new { status = "ok", duration_ms = 1200 });
        using var client = new OpenVipClient(http);

        var resp = await client.SpeakAsync("Hello", language: "en");

        Assert.Equal("ok", resp.Status);
        Assert.Equal(1200, resp.DurationMs);
    }

    // --- ControlAsync ---

    [Fact]
    public async Task StartListeningAsync_ReturnsAck()
    {
        var http = MockHttp(HttpStatusCode.OK, new { status = "ok" });
        using var client = new OpenVipClient(http);

        var ack = await client.StartListeningAsync();

        Assert.Equal("ok", ack.Status);
    }

    [Fact]
    public async Task StopListeningAsync_ReturnsAck()
    {
        var http = MockHttp(HttpStatusCode.OK, new { status = "ok" });
        using var client = new OpenVipClient(http);

        var ack = await client.StopListeningAsync();

        Assert.Equal("ok", ack.Status);
    }

    // --- SendMessageAsync ---

    [Fact]
    public async Task SendMessageAsync_ReturnsAck()
    {
        var http = MockHttp(HttpStatusCode.OK, new { status = "ok" });
        using var client = new OpenVipClient(http);

        var msg = MessageFactory.CreateTranscription("test message", language: "en");
        var ack = await client.SendMessageAsync("agent-1", msg);

        Assert.Equal("ok", ack.Status);
    }

    // --- SubscribeAsync ---

    [Fact]
    public async Task SubscribeAsync_YieldsMessages()
    {
        var sseData = "data: {\"type\":\"transcription\",\"text\":\"hello\"}\n\ndata: {\"type\":\"transcription\",\"text\":\"world\"}\n\n";
        var handler = new MockHandler(HttpStatusCode.OK, sseData, "text/event-stream");
        var http = new HttpClient(handler) { BaseAddress = new Uri("http://test:8770/openvip/") };
        using var client = new OpenVipClient(http);

        var messages = new List<AgentMessageDto>();
        await foreach (var msg in client.SubscribeAsync("test"))
            messages.Add(msg);

        Assert.Equal(2, messages.Count);
        Assert.Equal("hello", messages[0].Text);
        Assert.Equal("world", messages[1].Text);
    }

    [Fact]
    public async Task SubscribeAsync_ThrowsDuplicateAgentErrorOn409()
    {
        var handler = new MockHandler(HttpStatusCode.Conflict, "{}");
        var http = new HttpClient(handler) { BaseAddress = new Uri("http://test:8770/openvip/") };
        using var client = new OpenVipClient(http);

        await Assert.ThrowsAsync<DuplicateAgentError>(async () =>
        {
            await foreach (var _ in client.SubscribeAsync("test")) { }
        });
    }

    // --- StopSpeechAsync ---

    [Fact]
    public async Task StopSpeechAsync_ReturnsAck()
    {
        var http = MockHttp(HttpStatusCode.OK, new { status = "ok" });
        using var client = new OpenVipClient(http);

        var ack = await client.StopSpeechAsync();

        Assert.Equal("ok", ack.Status);
    }
}

/// <summary>
/// Tests for the MessageFactory.
/// </summary>
public class MessageFactoryTests
{
    [Fact]
    public void CreateTranscription_SetsProtocolFields()
    {
        var msg = MessageFactory.CreateTranscription("hello", language: "en");

        Assert.Equal("1.0", msg.Openvip);
        Assert.Equal("transcription", msg.Type);
        Assert.Equal("hello", msg.Text);
        Assert.Equal("en", msg.Language);
        Assert.NotEqual(Guid.Empty, msg.Id);
        Assert.True(msg.Timestamp <= DateTime.UtcNow);
    }

    [Fact]
    public void CreateTranscription_OptionalFieldsAreNull()
    {
        var msg = MessageFactory.CreateTranscription("test");

        Assert.Null(msg.Language);
        Assert.Null(msg.Confidence);
        Assert.Null(msg.Partial);
        Assert.Null(msg.Origin);
        Assert.Null(msg.TraceId);
        Assert.Null(msg.ParentId);
    }

    [Fact]
    public void CreateSpeechRequest_SetsProtocolFields()
    {
        var req = MessageFactory.CreateSpeechRequest("speak this", language: "it");

        Assert.Equal("1.0", req.Openvip);
        Assert.Equal("speech", req.Type);
        Assert.Equal("speak this", req.Text);
        Assert.Equal("it", req.Language);
    }

    [Fact]
    public void CreateTranscription_UniqueIds()
    {
        var msg1 = MessageFactory.CreateTranscription("a");
        var msg2 = MessageFactory.CreateTranscription("b");

        Assert.NotEqual(msg1.Id, msg2.Id);
    }
}

/// <summary>
/// Mock HttpMessageHandler for testing.
/// </summary>
internal class MockHandler : HttpMessageHandler
{
    private readonly HttpStatusCode? _status;
    private readonly string _content;
    private readonly string _contentType;
    private readonly HttpRequestException? _exception;

    public MockHandler(HttpStatusCode status, string content, string contentType = "application/json")
    {
        _status = status;
        _content = content;
        _contentType = contentType;
    }

    public MockHandler(HttpRequestException exception)
    {
        _exception = exception;
        _content = "";
        _contentType = "application/json";
    }

    protected override Task<HttpResponseMessage> SendAsync(
        HttpRequestMessage request, CancellationToken ct)
    {
        if (_exception != null)
            throw _exception;

        var response = new HttpResponseMessage(_status!.Value)
        {
            Content = new StringContent(_content, Encoding.UTF8, _contentType),
        };
        return Task.FromResult(response);
    }
}
