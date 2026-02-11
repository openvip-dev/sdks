#!/usr/bin/env python3
"""OpenVIP Python SDK demo.

Connects to a local OpenVIP engine (e.g. VoxType) and demonstrates
all SDK features: status, control, speech, messaging, and subscription.

Usage:
    pip install -e ../../python
    python demo.py
"""

from __future__ import annotations

import sys
import threading
import time

from openvip import Client, create_transcription


def main() -> None:
    url = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8770"
    client = Client(url, timeout=5.0)

    print(f"OpenVIP Python SDK demo")
    print(f"Connecting to {url}...")
    print()

    # 1. Status
    print("=== GET /status ===")
    try:
        status = client.get_status()
        print(f"  Protocol: {status.protocol_version}")
        print(f"  Agents:   {status.connected_agents}")
        if status.platform:
            print(f"  Platform: {status.platform}")
    except Exception as e:
        print(f"  Error: {e}")
        print("  Is the engine running? Start VoxType with: voxtype listen --agents")
        sys.exit(1)
    print()

    # 2. Control — start listening
    print("=== POST /control (stt.start) ===")
    try:
        ack = client.start_listening()
        print(f"  Response: {ack.status}")
    except Exception as e:
        print(f"  Error: {e}")
    print()

    # 3. Speech — text-to-speech
    print("=== POST /speech ===")
    try:
        resp = client.speak("Hello from the OpenVIP SDK!", language="en")
        print(f"  Status:   {resp.status}")
        print(f"  Duration: {resp.duration_ms}ms")
    except Exception as e:
        print(f"  Error: {e}")
    print()

    # 4. Send message to an agent
    print("=== POST /agents/demo/messages ===")
    msg = create_transcription(
        "This is a test message from the SDK demo",
        language="en",
        confidence=0.99,
    )
    try:
        ack = client.send_message("demo", msg)
        print(f"  Response: {ack.status}")
    except Exception as e:
        print(f"  Error: {e} (expected if no 'demo' agent connected)")
    print()

    # 5. Subscribe (SSE) — runs for 5 seconds
    print("=== GET /agents/sdk-demo/messages (SSE, 5 seconds) ===")
    print("  Listening for messages...")

    stop = threading.Event()

    def listen() -> None:
        try:
            for message in client.subscribe("sdk-demo"):
                if stop.is_set():
                    break
                print(f"  Received: '{message.text}' (lang={message.language})")
        except Exception:
            pass  # Connection closed

    thread = threading.Thread(target=listen, daemon=True)
    thread.start()
    time.sleep(5)
    stop.set()
    print("  Done.")
    print()

    # 6. Control — stop listening
    print("=== POST /control (stt.stop) ===")
    try:
        ack = client.stop_listening()
        print(f"  Response: {ack.status}")
    except Exception as e:
        print(f"  Error: {e}")
    print()

    print("Demo complete!")


if __name__ == "__main__":
    main()
