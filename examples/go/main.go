// OpenVIP Go SDK demo
// Usage: go run main.go [NAME]

package main

import (
	"context"
	"fmt"
	"os"
	"os/signal"

	openvip "github.com/openvip-dev/sdks"
)

func main() {
	name := "demo"
	if len(os.Args) > 1 {
		name = os.Args[1]
	}

	ctx, cancel := signal.NotifyContext(context.Background(), os.Interrupt)
	defer cancel()

	client := openvip.NewClient("http://localhost:8770/openvip", nil)

	// Watch which agent has focus and print a message when it changes
	go func() {
		statusCh, _ := client.SubscribeStatus(ctx, &openvip.SubscribeOptions{Reconnect: true})
		wasFocused := false
		first := true

		for status := range statusCh {
			currentAgent := ""
			if output, ok := status.Platform["output"].(map[string]interface{}); ok {
				if agent, ok := output["current_agent"].(string); ok {
					currentAgent = agent
				}
			}

			isFocused := currentAgent == name
			if isFocused != wasFocused || first {
				first = false
				wasFocused = isFocused
				if isFocused {
					fmt.Println("[agent] Hey, I'm here!")
				} else {
					fmt.Println("[agent] Ok, I'll wait here.")
				}
			}
		}
	}()

	// Listen for transcriptions and echo them back via TTS
	messageCh, _ := client.Subscribe(ctx, name, &openvip.SubscribeOptions{Reconnect: true})

	for message := range messageCh {
		fmt.Printf("[user ] %s\n", message.Text)

		if message.Text != "" {
			client.Speak(ctx, fmt.Sprintf("You said: %s", message.Text), &openvip.SpeakOptions{Language: "en"})
		}
	}
}
