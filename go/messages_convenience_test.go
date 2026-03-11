package openvip

import (
	"testing"
	"time"
)

func TestNewTranscriptionMessage(t *testing.T) {
	msg := NewTranscriptionMessage("hello world")

	if msg.Text != "hello world" {
		t.Errorf("expected text 'hello world', got %q", msg.Text)
	}
	if msg.Openvip != ProtocolVersion {
		t.Errorf("expected openvip %q, got %q", ProtocolVersion, msg.Openvip)
	}
	if msg.Type != "transcription" {
		t.Errorf("expected type 'transcription', got %q", msg.Type)
	}
	if msg.Id == "" {
		t.Error("expected non-empty id")
	}
	if time.Since(msg.Timestamp) > 2*time.Second {
		t.Errorf("expected recent timestamp, got %v", msg.Timestamp)
	}
}

func TestNewTranscriptionMessage_UniqueIDs(t *testing.T) {
	a := NewTranscriptionMessage("a")
	b := NewTranscriptionMessage("b")
	if a.Id == b.Id {
		t.Errorf("expected unique IDs, both got %q", a.Id)
	}
}

func TestNewSpeechRequestMessage(t *testing.T) {
	lang := "en"
	msg := NewSpeechRequestMessage("say this", &lang)

	if msg.Text != "say this" {
		t.Errorf("expected text 'say this', got %q", msg.Text)
	}
	if msg.Openvip != ProtocolVersion {
		t.Errorf("expected openvip %q, got %q", ProtocolVersion, msg.Openvip)
	}
	if msg.Type != "speech" {
		t.Errorf("expected type 'speech', got %q", msg.Type)
	}
	if msg.Id == "" {
		t.Error("expected non-empty id")
	}
	if time.Since(msg.Timestamp) > 2*time.Second {
		t.Errorf("expected recent timestamp, got %v", msg.Timestamp)
	}
	if msg.Language == nil || *msg.Language != "en" {
		t.Errorf("expected language 'en', got %v", msg.Language)
	}
}

func TestNewSpeechRequestMessage_NoLanguage(t *testing.T) {
	msg := NewSpeechRequestMessage("say this", nil)

	if msg.Language != nil {
		t.Errorf("expected nil language, got %q", *msg.Language)
	}
}

func TestNewControlRequestMessage(t *testing.T) {
	req := NewControlRequestMessage("stt.start")

	if req.Command != "stt.start" {
		t.Errorf("expected command 'stt.start', got %q", req.Command)
	}
	if req.Openvip != ProtocolVersion {
		t.Errorf("expected openvip %q, got %q", ProtocolVersion, req.Openvip)
	}
	if req.Id == "" {
		t.Error("expected non-empty id")
	}
}

func TestNewControlRequestMessage_UniqueIDs(t *testing.T) {
	a := NewControlRequestMessage("stt.start")
	b := NewControlRequestMessage("stt.stop")
	if a.Id == b.Id {
		t.Errorf("expected unique IDs, both got %q", a.Id)
	}
}
