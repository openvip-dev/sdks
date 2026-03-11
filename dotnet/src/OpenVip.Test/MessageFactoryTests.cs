using Xunit;

namespace OpenVip.Test;

public class MessageFactoryTests
{
    [Fact]
    public void CreateTranscription_SetsTextAndProtocolFields()
    {
        var msg = MessageFactory.CreateTranscription("hello world");
        Assert.Equal("hello world", msg.Text);
        Assert.Equal("1.0", msg.Openvip);
        Assert.Equal("transcription", msg.Type);
        Assert.NotEqual(Guid.Empty, msg.Id);
    }

    [Fact]
    public void CreateTranscription_GeneratesUniqueIds()
    {
        var a = MessageFactory.CreateTranscription("a");
        var b = MessageFactory.CreateTranscription("b");
        Assert.NotEqual(a.Id, b.Id);
    }

    [Fact]
    public void CreateTranscription_SetsTimestamp()
    {
        var before = DateTime.UtcNow;
        var msg = MessageFactory.CreateTranscription("test");
        var after = DateTime.UtcNow;
        Assert.InRange(msg.Timestamp, before, after);
    }

    [Fact]
    public void CreateTranscription_SetsOptionalFields()
    {
        var msg = MessageFactory.CreateTranscription("test", language: "en", confidence: 0.95);
        Assert.Equal("en", msg.Language);
        Assert.Equal(0.95, msg.Confidence);
    }

    [Fact]
    public void CreateSpeechRequest_SetsTextAndProtocolFields()
    {
        var req = MessageFactory.CreateSpeechRequest("hello");
        Assert.Equal("hello", req.Text);
        Assert.Equal("1.0", req.Openvip);
        Assert.Equal("speech", req.Type);
        Assert.NotEqual(Guid.Empty, req.Id);
    }

    [Fact]
    public void CreateSpeechRequest_SetsLanguage()
    {
        var req = MessageFactory.CreateSpeechRequest("ciao", language: "it");
        Assert.Equal("it", req.Language);
    }

    [Fact]
    public void CreateControlRequest_SetsCommandAndProtocolFields()
    {
        var req = MessageFactory.CreateControlRequest("stt.start");
        Assert.Equal("stt.start", req.Command);
        Assert.Equal("1.0", req.Openvip);
        Assert.NotEqual(Guid.Empty, req.Id);
    }

    [Fact]
    public void CreateControlRequest_GeneratesUniqueIds()
    {
        var a = MessageFactory.CreateControlRequest("stt.start");
        var b = MessageFactory.CreateControlRequest("stt.start");
        Assert.NotEqual(a.Id, b.Id);
    }
}
