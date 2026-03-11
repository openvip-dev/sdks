// High-level OpenVIP client for .NET.
//
// Usage:
//   using var client = new OpenVipClient("http://localhost:8770");
//   var response = await client.SpeakAsync("Hello world", language: "en");
//   var status = await client.GetStatusAsync();
//   await client.StartListeningAsync();
//
//   await foreach (var msg in client.SubscribeAsync("my-agent"))
//       Console.WriteLine($"[{msg.Type}] {msg.Text}");

using System.Net.Http.Json;
using System.Runtime.CompilerServices;
using System.Text.Json;
using System.Text.Json.Serialization;
using System.Threading.Channels;

namespace OpenVip;

/// <summary>
/// Raised when an agent ID is already connected (HTTP 409).
/// </summary>
public class DuplicateAgentError : Exception
{
    public DuplicateAgentError(string message) : base(message) { }
    public DuplicateAgentError(string message, Exception inner) : base(message, inner) { }
}

/// <summary>
/// Options for SSE subscribe methods.
/// </summary>
public class SubscribeOptions
{
    /// <summary>Auto-reconnect on connection loss with exponential backoff.</summary>
    public bool Reconnect { get; init; }

    /// <summary>Initial delay between reconnection attempts in seconds.</summary>
    public double RetryDelay { get; init; } = 0.5;

    /// <summary>Maximum delay between reconnection attempts in seconds.</summary>
    public double MaxRetryDelay { get; init; } = 5.0;
}

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
    private readonly string? _token;

    /// <summary>
    /// Create a new OpenVIP client.
    /// </summary>
    /// <param name="url">Base URL of the OpenVIP engine.</param>
    /// <param name="token">Optional Bearer token for authentication.</param>
    public OpenVipClient(string url = "http://localhost:8770/openvip", string? token = null)
    {
        _http = new HttpClient { BaseAddress = new Uri(url.TrimEnd('/')) };
        _ownsHttpClient = true;
        _token = token;
        if (token != null)
            _http.DefaultRequestHeaders.Authorization =
                new System.Net.Http.Headers.AuthenticationHeaderValue("Bearer", token);
    }

    /// <summary>
    /// Create a new OpenVIP client with an existing HttpClient.
    /// </summary>
    public OpenVipClient(HttpClient httpClient)
    {
        _http = httpClient;
        _ownsHttpClient = false;
    }

    // --- Status ---

    /// <summary>Get engine status.</summary>
    public async Task<StatusDto> GetStatusAsync(CancellationToken ct = default)
    {
        var resp = await _http.GetFromJsonAsync<StatusDto>("/status", JsonOptions, ct)
            ?? throw new InvalidOperationException("Empty response");
        return resp;
    }

    /// <summary>Check if the engine is reachable.</summary>
    public async Task<bool> IsAvailableAsync(CancellationToken ct = default)
    {
        try
        {
            await GetStatusAsync(ct);
            return true;
        }
        catch (HttpRequestException)
        {
            return false;
        }
        catch (TaskCanceledException)
        {
            return false;
        }
    }

    // --- Speech ---

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

    /// <summary>Stop the currently playing TTS audio.</summary>
    public async Task<AckDto> StopSpeechAsync(CancellationToken ct = default)
    {
        var resp = await _http.PostAsJsonAsync("/speech/stop", new { }, JsonOptions, ct);
        resp.EnsureSuccessStatusCode();
        return await resp.Content.ReadFromJsonAsync<AckDto>(JsonOptions, ct)
            ?? throw new InvalidOperationException("Empty response");
    }

    // --- Control ---

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

    // --- Messages ---

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

    // --- SSE Subscribe ---

    /// <summary>
    /// Subscribe to messages for an agent via SSE.
    /// The SSE connection acts as agent registration — the agent exists
    /// as long as the enumeration is active.
    /// </summary>
    /// <param name="agentId">Agent identifier to register.</param>
    /// <param name="options">Reconnection options.</param>
    /// <param name="ct">Cancellation token to stop the stream.</param>
    /// <returns>Async enumerable of agent messages.</returns>
    /// <exception cref="DuplicateAgentError">If the agent ID is already connected (HTTP 409).</exception>
    public IAsyncEnumerable<AgentMessageDto> SubscribeAsync(
        string agentId,
        SubscribeOptions? options = null,
        CancellationToken ct = default)
    {
        var url = $"/agents/{agentId}/messages";
        return SseStreamAsync<AgentMessageDto>(
            url, options ?? new SubscribeOptions(), ct,
            conflictMessage: $"Agent '{agentId}' is already connected");
    }

    /// <summary>
    /// Subscribe to status changes via SSE.
    /// Events are sent only on state transitions.
    /// </summary>
    public IAsyncEnumerable<StatusDto> SubscribeStatusAsync(
        SubscribeOptions? options = null,
        CancellationToken ct = default)
    {
        return SseStreamAsync<StatusDto>(
            "/status/stream", options ?? new SubscribeOptions(), ct);
    }

    // --- SSE helper ---

    private IAsyncEnumerable<T> SseStreamAsync<T>(
        string path,
        SubscribeOptions options,
        CancellationToken ct,
        string? conflictMessage = null)
    {
        var channel = Channel.CreateUnbounded<T>();

        _ = Task.Run(async () =>
        {
            var currentDelay = options.RetryDelay;

            try
            {
                while (!ct.IsCancellationRequested)
                {
                    HttpResponseMessage? response = null;
                    try
                    {
                        var request = new HttpRequestMessage(HttpMethod.Get, path);
                        request.Headers.Accept.Add(
                            new System.Net.Http.Headers.MediaTypeWithQualityHeaderValue("text/event-stream"));

                        response = await _http.SendAsync(
                            request, HttpCompletionOption.ResponseHeadersRead, ct);

                        if (response.StatusCode == System.Net.HttpStatusCode.Conflict)
                        {
                            var msg = conflictMessage ?? $"SSE conflict (409) for {path}";
                            channel.Writer.Complete(new DuplicateAgentError(msg));
                            return;
                        }
                        response.EnsureSuccessStatusCode();

                        currentDelay = options.RetryDelay; // Reset on success

                        using var stream = await response.Content.ReadAsStreamAsync(ct);
                        using var reader = new StreamReader(stream);

                        while (!ct.IsCancellationRequested)
                        {
                            var line = await reader.ReadLineAsync(ct);
                            if (line == null) break; // Stream ended

                            if (!line.StartsWith("data: ")) continue;

                            var payload = line[6..];
                            try
                            {
                                var parsed = JsonSerializer.Deserialize<T>(payload, JsonOptions);
                                if (parsed != null)
                                    await channel.Writer.WriteAsync(parsed, ct);
                            }
                            catch (JsonException)
                            {
                                continue;
                            }
                        }

                        // Stream ended cleanly
                        if (!options.Reconnect)
                        {
                            channel.Writer.Complete();
                            return;
                        }
                    }
                    catch (OperationCanceledException) when (ct.IsCancellationRequested)
                    {
                        channel.Writer.Complete();
                        return;
                    }
                    catch (HttpRequestException) when (!options.Reconnect)
                    {
                        throw;
                    }
                    catch (IOException) when (!options.Reconnect)
                    {
                        throw;
                    }
                    catch (HttpRequestException)
                    {
                        // Will reconnect
                    }
                    catch (IOException)
                    {
                        // Will reconnect
                    }
                    finally
                    {
                        response?.Dispose();
                    }

                    // Reconnect with exponential backoff
                    if (ct.IsCancellationRequested) break;
                    await Task.Delay(TimeSpan.FromSeconds(currentDelay), ct);
                    currentDelay = Math.Min(currentDelay * 2, options.MaxRetryDelay);
                }

                channel.Writer.Complete();
            }
            catch (Exception ex)
            {
                channel.Writer.Complete(ex);
            }
        }, ct);

        return channel.Reader.ReadAllAsync(ct);
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

/// <summary>
/// Represents a message received from the SSE agent stream.
/// Can be a transcription or a speech request.
/// </summary>
public record AgentMessageDto
{
    public string Type { get; init; } = "";
    public string? Id { get; init; }
    public string? Timestamp { get; init; }
    public string Text { get; init; } = "";
    public string? Language { get; init; }
    public double? Confidence { get; init; }
    public bool? Partial { get; init; }
    public string? Origin { get; init; }
}
