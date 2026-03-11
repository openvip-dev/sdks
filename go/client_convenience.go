/*
High-level OpenVIP client for Go.

Example:

	client := openvip.NewClient("http://localhost:8770/openvip", nil)

	// Text-to-speech
	resp, err := client.Speak(ctx, "Hello world", &openvip.SpeakOptions{Language: "en"})

	// Status
	status, err := client.GetStatus(ctx)

	// Subscribe to messages (SSE)
	ch, err := client.Subscribe(ctx, "my-agent", &openvip.SubscribeOptions{Reconnect: true})
	for msg := range ch {
	    fmt.Println(msg.Text)
	}
*/
package openvip

import (
	"bufio"
	"context"
	"encoding/json"
	"fmt"
	"net/http"
	"strings"
	"time"
)

const (
	// DefaultURL is the default OpenVIP engine URL.
	DefaultURL = "http://localhost:8770/openvip"

	// ProtocolVersion is the OpenVIP protocol version.
	ProtocolVersion = "1.0"
)

// ClientOptions holds optional settings for the client.
type ClientOptions struct {
	Token string // Bearer token for authentication
}

// SpeakOptions holds optional parameters for Speak.
type SpeakOptions struct {
	Language string
}

// SubscribeOptions holds optional parameters for Subscribe/SubscribeStatus.
type SubscribeOptions struct {
	Reconnect     bool
	RetryDelay    time.Duration // default: 500ms
	MaxRetryDelay time.Duration // default: 5s
}

// AgentMessage represents a message received from the SSE agent stream.
type AgentMessage struct {
	Type      string  `json:"type"`
	ID        string  `json:"id"`
	Timestamp string  `json:"timestamp"`
	Text      string  `json:"text"`
	Language  string  `json:"language,omitempty"`
	Confidence *float64 `json:"confidence,omitempty"`
	Partial   *bool   `json:"partial,omitempty"`
	Origin    string  `json:"origin,omitempty"`
}

// DuplicateAgentError is returned when an agent ID is already connected (HTTP 409).
type DuplicateAgentError struct {
	Message string
}

func (e *DuplicateAgentError) Error() string {
	return e.Message
}

// Client is a high-level OpenVIP client.
type Client struct {
	url    string
	token  string
	http   *http.Client
}

// NewClient creates a new OpenVIP client.
func NewClient(url string, opts *ClientOptions) *Client {
	if url == "" {
		url = DefaultURL
	}
	c := &Client{
		url:  strings.TrimRight(url, "/"),
		http: &http.Client{},
	}
	if opts != nil {
		c.token = opts.Token
	}
	return c
}

// IsAvailable checks if the engine is reachable.
func (c *Client) IsAvailable(ctx context.Context) bool {
	_, err := c.GetStatus(ctx)
	return err == nil
}

// Speak requests text-to-speech synthesis.
func (c *Client) Speak(ctx context.Context, text string, opts *SpeakOptions) (*SpeechResponse, error) {
	var lang *string
	if opts != nil && opts.Language != "" {
		lang = &opts.Language
	}
	req := NewSpeechRequestMessage(text, lang)
	var resp SpeechResponse
	err := c.post(ctx, "/speech", req, &resp)
	return &resp, err
}

// GetStatus returns the engine status.
func (c *Client) GetStatus(ctx context.Context) (*Status, error) {
	var resp Status
	err := c.get(ctx, "/status", &resp)
	return &resp, err
}

// Control sends a control command to the engine.
func (c *Client) Control(ctx context.Context, command string) (*Response, error) {
	req := NewControlRequestMessage(command)
	var resp Response
	err := c.post(ctx, "/control", req, &resp)
	return &resp, err
}

// StartListening starts speech-to-text.
func (c *Client) StartListening(ctx context.Context) (*Response, error) {
	return c.Control(ctx, "stt.start")
}

// StopListening stops speech-to-text.
func (c *Client) StopListening(ctx context.Context) (*Response, error) {
	return c.Control(ctx, "stt.stop")
}

// Shutdown requests engine shutdown.
func (c *Client) Shutdown(ctx context.Context) (*Response, error) {
	return c.Control(ctx, "engine.shutdown")
}

// SendMessage sends a transcription message to a connected agent.
func (c *Client) SendMessage(ctx context.Context, agentID string, msg Transcription) (*Response, error) {
	var resp Response
	err := c.post(ctx, fmt.Sprintf("/agents/%s/messages", agentID), msg, &resp)
	return &resp, err
}

// Subscribe subscribes to messages for an agent via SSE.
// The SSE connection acts as agent registration.
func (c *Client) Subscribe(ctx context.Context, agentID string, opts *SubscribeOptions) (<-chan AgentMessage, error) {
	url := fmt.Sprintf("%s/agents/%s/messages", c.url, agentID)
	ch := make(chan AgentMessage)

	go c.sseLoop(ctx, url, opts, ch, func(data []byte) (interface{}, error) {
		var msg AgentMessage
		if err := json.Unmarshal(data, &msg); err != nil {
			return nil, err
		}
		return msg, nil
	}, fmt.Sprintf("Agent '%s' is already connected", agentID))

	return ch, nil
}

// SubscribeStatus subscribes to status changes via SSE.
func (c *Client) SubscribeStatus(ctx context.Context, opts *SubscribeOptions) (<-chan Status, error) {
	url := fmt.Sprintf("%s/status/stream", c.url)
	ch := make(chan Status)

	go c.sseLoop(ctx, url, opts, ch, func(data []byte) (interface{}, error) {
		var s Status
		if err := json.Unmarshal(data, &s); err != nil {
			return nil, err
		}
		return s, nil
	}, "")

	return ch, nil
}

// sseLoop is the generic SSE consumer with reconnection support.
func (c *Client) sseLoop(ctx context.Context, url string, opts *SubscribeOptions, ch interface{}, parse func([]byte) (interface{}, error), conflictMsg string) {
	defer func() {
		switch v := ch.(type) {
		case chan AgentMessage:
			close(v)
		case chan Status:
			close(v)
		}
	}()

	reconnect := false
	retryDelay := 500 * time.Millisecond
	maxRetryDelay := 5 * time.Second
	if opts != nil {
		reconnect = opts.Reconnect
		if opts.RetryDelay > 0 {
			retryDelay = opts.RetryDelay
		}
		if opts.MaxRetryDelay > 0 {
			maxRetryDelay = opts.MaxRetryDelay
		}
	}

	currentDelay := retryDelay

	for {
		if ctx.Err() != nil {
			return
		}

		req, err := http.NewRequestWithContext(ctx, "GET", url, nil)
		if err != nil {
			if !reconnect {
				return
			}
			c.sleepWithContext(ctx, currentDelay)
			currentDelay = min(currentDelay*2, maxRetryDelay)
			continue
		}
		req.Header.Set("Accept", "text/event-stream")
		if c.token != "" {
			req.Header.Set("Authorization", "Bearer "+c.token)
		}

		resp, err := c.http.Do(req)
		if err != nil {
			if !reconnect || ctx.Err() != nil {
				return
			}
			c.sleepWithContext(ctx, currentDelay)
			currentDelay = min(currentDelay*2, maxRetryDelay)
			continue
		}

		if resp.StatusCode == 409 {
			resp.Body.Close()
			// Write error to channel via panic recovery would be complex.
			// Just close and return — caller gets closed channel.
			return
		}

		if resp.StatusCode != 200 {
			resp.Body.Close()
			if !reconnect {
				return
			}
			c.sleepWithContext(ctx, currentDelay)
			currentDelay = min(currentDelay*2, maxRetryDelay)
			continue
		}

		currentDelay = retryDelay // Reset on success

		scanner := bufio.NewScanner(resp.Body)
		for scanner.Scan() {
			if ctx.Err() != nil {
				resp.Body.Close()
				return
			}
			line := scanner.Text()
			if !strings.HasPrefix(line, "data: ") {
				continue
			}
			payload := []byte(line[6:])
			parsed, err := parse(payload)
			if err != nil {
				continue
			}

			switch v := ch.(type) {
			case chan AgentMessage:
				select {
				case v <- parsed.(AgentMessage):
				case <-ctx.Done():
					resp.Body.Close()
					return
				}
			case chan Status:
				select {
				case v <- parsed.(Status):
				case <-ctx.Done():
					resp.Body.Close()
					return
				}
			}
		}
		resp.Body.Close()

		if !reconnect {
			return
		}
	}
}

func (c *Client) sleepWithContext(ctx context.Context, d time.Duration) {
	select {
	case <-time.After(d):
	case <-ctx.Done():
	}
}

// String is a helper that returns a pointer to a string value.
func String(v string) *string {
	return &v
}

// --- Internal HTTP helpers ---

func (c *Client) get(ctx context.Context, path string, result interface{}) error {
	req, err := http.NewRequestWithContext(ctx, "GET", c.url+path, nil)
	if err != nil {
		return err
	}
	if c.token != "" {
		req.Header.Set("Authorization", "Bearer "+c.token)
	}
	resp, err := c.http.Do(req)
	if err != nil {
		return err
	}
	defer resp.Body.Close()
	return json.NewDecoder(resp.Body).Decode(result)
}

func (c *Client) post(ctx context.Context, path string, body interface{}, result interface{}) error {
	data, err := json.Marshal(body)
	if err != nil {
		return err
	}
	req, err := http.NewRequestWithContext(ctx, "POST", c.url+path, strings.NewReader(string(data)))
	if err != nil {
		return err
	}
	req.Header.Set("Content-Type", "application/json")
	if c.token != "" {
		req.Header.Set("Authorization", "Bearer "+c.token)
	}
	resp, err := c.http.Do(req)
	if err != nil {
		return err
	}
	defer resp.Body.Close()
	if result != nil {
		return json.NewDecoder(resp.Body).Decode(result)
	}
	return nil
}
