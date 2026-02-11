// High-level OpenVIP client for .NET.
//
// Usage:
//   using var client = new OpenVipClient("http://localhost:8770");
//   var response = await client.SpeakAsync("Hello world", language: "en");
//   var status = await client.GetStatusAsync();
//   await client.StartListeningAsync();
//
//   var msg = MessageFactory.CreateTranscription("turn on the light", language: "en");
//   await client.SendMessageAsync("my-agent", msg);

using System.Net.Http.Json;
using System.Text.Json;
using System.Text.Json.Serialization;

namespace OpenVip;

/// <summary>
/// High-level OpenVIP HTTP client.
/// Provides a simple API without requiring DI setup.
/// </summary>
public class OpenVipClient : IDisposable
{
    private static readonly JsonSerializerOptions JsonOptions = new()
    {
        PropertyNamingPolicy = JsonNamingPolicy.SnakeCaseLower,
        DefaultIgnoreCondition = JsonIgnoreCondition.WhenWritingNull,
    };

    private readonly HttpClient _http;
    private readonly bool _ownsHttpClient;

    /// <summary>
    /// Create a new OpenVIP client.
    /// </summary>
    /// <param name="url">Base URL of the OpenVIP engine.</param>
    public OpenVipClient(string url = "http://localhost:8770")
    {
        _http = new HttpClient { BaseAddress = new Uri(url.TrimEnd('/')) };
        _ownsHttpClient = true;
    }

    /// <summary>
    /// Create a new OpenVIP client with an existing HttpClient.
    /// </summary>
    public OpenVipClient(HttpClient httpClient)
    {
        _http = httpClient;
        _ownsHttpClient = false;
    }

    /// <summary>Request text-to-speech synthesis.</summary>
    public async Task<SpeechResponseDto> SpeakAsync(
        string text,
        string? language = null,
        CancellationToken ct = default)
    {
        var req = MessageFactory.CreateSpeechRequest(text, language);
        var resp = await _http.PostAsJsonAsync("/speech", req, JsonOptions, ct);
        resp.EnsureSuccessStatusCode();
        return await resp.Content.ReadFromJsonAsync<SpeechResponseDto>(JsonOptions, ct)
            ?? throw new InvalidOperationException("Empty response");
    }

    /// <summary>Get engine status.</summary>
    public async Task<StatusDto> GetStatusAsync(CancellationToken ct = default)
    {
        var resp = await _http.GetFromJsonAsync<StatusDto>("/status", JsonOptions, ct)
            ?? throw new InvalidOperationException("Empty response");
        return resp;
    }

    /// <summary>Send a control command.</summary>
    public async Task<AckDto> ControlAsync(string command, CancellationToken ct = default)
    {
        var body = new { command };
        var resp = await _http.PostAsJsonAsync("/control", body, JsonOptions, ct);
        resp.EnsureSuccessStatusCode();
        return await resp.Content.ReadFromJsonAsync<AckDto>(JsonOptions, ct)
            ?? throw new InvalidOperationException("Empty response");
    }

    /// <summary>Start speech-to-text.</summary>
    public Task<AckDto> StartListeningAsync(CancellationToken ct = default)
        => ControlAsync("stt.start", ct);

    /// <summary>Stop speech-to-text.</summary>
    public Task<AckDto> StopListeningAsync(CancellationToken ct = default)
        => ControlAsync("stt.stop", ct);

    /// <summary>Request engine shutdown.</summary>
    public Task<AckDto> ShutdownAsync(CancellationToken ct = default)
        => ControlAsync("engine.shutdown", ct);

    /// <summary>Send a message to a connected agent.</summary>
    public async Task<AckDto> SendMessageAsync(
        string agentId,
        TranscriptionDto message,
        CancellationToken ct = default)
    {
        var resp = await _http.PostAsJsonAsync($"/agents/{agentId}/messages", message, JsonOptions, ct);
        resp.EnsureSuccessStatusCode();
        return await resp.Content.ReadFromJsonAsync<AckDto>(JsonOptions, ct)
            ?? throw new InvalidOperationException("Empty response");
    }

    public void Dispose()
    {
        if (_ownsHttpClient)
            _http.Dispose();
    }
}

// Simple DTOs for the convenience client (independent from generated DI-heavy models)

public record SpeechResponseDto(string Status, int? DurationMs);

public record StatusDto(
    string? ProtocolVersion,
    List<string>? ConnectedAgents,
    Dictionary<string, JsonElement>? Platform);

public record AckDto(string Status, string? Id);

public record TranscriptionDto(
    string Openvip,
    string Type,
    Guid Id,
    DateTime Timestamp,
    string Text,
    string? Language = null,
    double? Confidence = null,
    bool? Partial = null,
    string? Origin = null,
    Guid? TraceId = null,
    Guid? ParentId = null);

public record SpeechRequestDto(
    string Openvip,
    string Type,
    string Text,
    string? Language = null);
