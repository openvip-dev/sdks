/*
Convenience factories for OpenVIP messages.

Example:

	msg := openvip.NewTranscriptionMessage("hello world")
	msg.SetLanguage("en")
	msg.SetConfidence(0.95)

	req := openvip.NewSpeechRequestMessage("hello world", openvip.String("en"))
*/
package openvip

import (
	"crypto/rand"
	"fmt"
	"time"
)

// NewTranscriptionMessage creates a Transcription with auto-filled protocol fields.
// Generates a random UUID for id and uses current UTC time for timestamp.
func NewTranscriptionMessage(text string) *Transcription {
	id := generateUUID()
	now := time.Now().UTC()
	return NewTranscription(ProtocolVersion, "transcription", id, now, text)
}

// NewSpeechRequestMessage creates a SpeechRequest with auto-filled protocol fields.
// Language is optional (pass nil to omit).
func NewSpeechRequestMessage(text string, language *string) *SpeechRequest {
	req := NewSpeechRequest(ProtocolVersion, "speech", text)
	if language != nil {
		req.SetLanguage(*language)
	}
	return req
}

// generateUUID generates a random UUID v4 string without external dependencies.
func generateUUID() string {
	var uuid [16]byte
	_, _ = rand.Read(uuid[:])
	uuid[6] = (uuid[6] & 0x0f) | 0x40 // version 4
	uuid[8] = (uuid[8] & 0x3f) | 0x80 // variant 10
	return fmt.Sprintf("%08x-%04x-%04x-%04x-%012x",
		uuid[0:4], uuid[4:6], uuid[6:8], uuid[8:10], uuid[10:16])
}
