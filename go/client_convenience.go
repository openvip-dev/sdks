/*
High-level OpenVIP client for Go.

Example:

	client := openvip.NewClient("http://localhost:8770")

	// Text-to-speech
	resp, err := client.Speak(ctx, "Hello world", openvip.String("en"))

	// Status
	status, err := client.GetStatus(ctx)

	// Control
	client.StartListening(ctx)
	client.StopListening(ctx)

	// Messages
	msg := openvip.NewTranscriptionMessage("turn on the light")
	msg.SetLanguage("en")
	client.SendMessage(ctx, "my-agent", *msg)
*/
package openvip

import (
	"context"
)

const (
	// DefaultURL is the default OpenVIP engine URL.
	DefaultURL = "http://localhost:8770"

	// ProtocolVersion is the OpenVIP protocol version.
	ProtocolVersion = "1.0"
)

// Client is a high-level OpenVIP client.
type Client struct {
	api *APIClient
}

// NewClient creates a new OpenVIP client.
// If url is empty, DefaultURL is used.
func NewClient(url string) *Client {
	if url == "" {
		url = DefaultURL
	}
	cfg := NewConfiguration()
	cfg.Servers = ServerConfigurations{
		{URL: url},
	}
	return &Client{api: NewAPIClient(cfg)}
}

// Speak requests text-to-speech synthesis.
// Language is optional (pass nil to use server default).
func (c *Client) Speak(ctx context.Context, text string, language *string) (*SpeechResponse, error) {
	req := *NewSpeechRequest(ProtocolVersion, "speech", text)
	if language != nil {
		req.SetLanguage(*language)
	}
	resp, _, err := c.api.SpeechAPI.TextToSpeech(ctx).SpeechRequest(req).Execute()
	return resp, err
}

// GetStatus returns the engine status.
func (c *Client) GetStatus(ctx context.Context) (*Status, error) {
	resp, _, err := c.api.StatusAPI.GetStatus(ctx).Execute()
	return resp, err
}

// Control sends a control command to the engine.
func (c *Client) Control(ctx context.Context, command string) (*Ack, error) {
	req := *NewControlRequest(command)
	resp, _, err := c.api.ControlAPI.SendControl(ctx).ControlRequest(req).Execute()
	return resp, err
}

// StartListening starts speech-to-text.
func (c *Client) StartListening(ctx context.Context) (*Ack, error) {
	return c.Control(ctx, "stt.start")
}

// StopListening stops speech-to-text.
func (c *Client) StopListening(ctx context.Context) (*Ack, error) {
	return c.Control(ctx, "stt.stop")
}

// Shutdown requests engine shutdown.
func (c *Client) Shutdown(ctx context.Context) (*Ack, error) {
	return c.Control(ctx, "engine.shutdown")
}

// SendMessage sends a transcription message to a connected agent.
func (c *Client) SendMessage(ctx context.Context, agentID string, msg Transcription) (*Ack, error) {
	resp, _, err := c.api.MessagesAPI.SendMessage(ctx, agentID).Transcription(msg).Execute()
	return resp, err
}

// String is a helper that returns a pointer to a string value.
// Useful for optional parameters: client.Speak(ctx, "hello", openvip.String("en"))
func String(v string) *string {
	return &v
}
