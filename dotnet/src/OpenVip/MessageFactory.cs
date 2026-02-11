// Convenience factories for OpenVIP messages.
//
// Usage:
//   var msg = MessageFactory.CreateTranscription("hello world", language: "en");
//   var req = MessageFactory.CreateSpeechRequest("hello world", language: "en");

namespace OpenVip;

/// <summary>
/// Factory methods for creating OpenVIP messages with auto-filled protocol fields.
/// </summary>
public static class MessageFactory
{
    /// <summary>OpenVIP protocol version.</summary>
    public const string ProtocolVersion = "1.0";

    /// <summary>
    /// Create a Transcription message with auto-filled id and timestamp.
    /// </summary>
    public static TranscriptionDto CreateTranscription(
        string text,
        string? language = null,
        double? confidence = null,
        bool? partial = null,
        string? origin = null,
        Guid? traceId = null,
        Guid? parentId = null)
    {
        return new TranscriptionDto(
            Openvip: ProtocolVersion,
            Type: "transcription",
            Id: Guid.NewGuid(),
            Timestamp: DateTime.UtcNow,
            Text: text,
            Language: language,
            Confidence: confidence,
            Partial: partial,
            Origin: origin,
            TraceId: traceId,
            ParentId: parentId);
    }

    /// <summary>
    /// Create a SpeechRequest with auto-filled protocol version.
    /// </summary>
    public static SpeechRequestDto CreateSpeechRequest(
        string text,
        string? language = null)
    {
        return new SpeechRequestDto(
            Openvip: ProtocolVersion,
            Type: "speech",
            Text: text,
            Language: language);
    }
}
