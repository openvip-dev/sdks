#!/usr/bin/env python3
"""OpenVIP Python SDK — minimal voice agent demo.

Subscribes as an agent, prints transcriptions, and echoes them back via TTS.
Press Ctrl+C to stop.

Usage:
    pip install openvip
    python demo.py [URL]
"""

import signal
import sys

from openvip import Client, DuplicateAgentError

url = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8770/openvip"
client = Client(url)

if not client.is_available():
    print(f"Engine not available at {url}")
    sys.exit(1)

status = client.get_status()
print(f"Connected — agents: {status.connected_agents}")
print("Listening for voice... (Ctrl+C to stop)\n")

try:
    for msg in client.subscribe("demo", reconnect=True):
        print(f"[{msg.type}] {msg.text}")
        if msg.text.strip():
            client.speak(f"You said: {msg.text}", language="en")
except DuplicateAgentError:
    print("Agent 'demo' is already connected.")
except KeyboardInterrupt:
    print("\nStopped.")
