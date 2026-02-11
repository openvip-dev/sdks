// OpenVIP Go SDK demo.
//
// Connects to a local OpenVIP engine (e.g. VoxType) and demonstrates
// SDK features: status, control, speech, and messaging.
//
// Usage:
//
//	go run main.go [http://localhost:8770]
package main

import (
	"context"
	"fmt"
	"os"
	"time"

	"github.com/google/uuid"
	openapi "github.com/openvip/go"
)

func main() {
	baseURL := "http://localhost:8770"
	if len(os.Args) > 1 {
		baseURL = os.Args[1]
	}

	config := openapi.NewConfiguration()
	config.Servers = openapi.ServerConfigurations{
		{URL: baseURL},
	}
	client := openapi.NewAPIClient(config)
	ctx := context.Background()

	fmt.Println("OpenVIP Go SDK demo")
	fmt.Printf("Connecting to %s...\n\n", baseURL)

	// 1. Status
	fmt.Println("=== GET /status ===")
	status, _, err := client.StatusAPI.GetStatus(ctx).Execute()
	if err != nil {
		fmt.Printf("  Error: %v\n", err)
		fmt.Println("  Is the engine running? Start VoxType with: voxtype listen --agents")
		os.Exit(1)
	}
	fmt.Printf("  Protocol: %s\n", *status.ProtocolVersion)
	fmt.Printf("  Agents:   %v\n", status.ConnectedAgents)
	fmt.Println()

	// 2. Control — start listening
	fmt.Println("=== POST /control (stt.start) ===")
	controlReq := *openapi.NewControlRequest("stt.start")
	ack, _, err := client.ControlAPI.SendControl(ctx).ControlRequest(controlReq).Execute()
	if err != nil {
		fmt.Printf("  Error: %v\n", err)
	} else {
		fmt.Printf("  Response: %s\n", ack.Status)
	}
	fmt.Println()

	// 3. Speech
	fmt.Println("=== POST /speech ===")
	speechReq := *openapi.NewSpeechRequest("1.0", "speech", "Hello from the OpenVIP Go SDK!")
	lang := "en"
	speechReq.Language = &lang
	speechResp, _, err := client.SpeechAPI.TextToSpeech(ctx).SpeechRequest(speechReq).Execute()
	if err != nil {
		fmt.Printf("  Error: %v\n", err)
	} else {
		fmt.Printf("  Status:   %s\n", speechResp.Status)
		if speechResp.DurationMs != nil {
			fmt.Printf("  Duration: %dms\n", *speechResp.DurationMs)
		}
	}
	fmt.Println()

	// 4. Send message
	fmt.Println("=== POST /agents/demo/messages ===")
	now := time.Now()
	msgID := uuid.New().String()
	msg := *openapi.NewTranscription("1.0", "transcription", msgID, now, "Test message from Go SDK demo")
	msg.Language = &lang
	ack2, _, err := client.MessagesAPI.SendMessage(ctx, "demo").Transcription(msg).Execute()
	if err != nil {
		fmt.Printf("  Error: %v (expected if no 'demo' agent connected)\n", err)
	} else {
		fmt.Printf("  Response: %s\n", ack2.Status)
	}
	fmt.Println()

	// 5. Control — stop listening
	fmt.Println("=== POST /control (stt.stop) ===")
	controlReq2 := *openapi.NewControlRequest("stt.stop")
	ack3, _, err := client.ControlAPI.SendControl(ctx).ControlRequest(controlReq2).Execute()
	if err != nil {
		fmt.Printf("  Error: %v\n", err)
	} else {
		fmt.Printf("  Response: %s\n", ack3.Status)
	}
	fmt.Println()

	fmt.Println("Demo complete!")
}
