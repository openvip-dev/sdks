# OpenVIP Python SDK demo
# Usage: uv run --with openvip python demo.py [NAME]

import sys
import threading
from openvip import Client

name = sys.argv[1] if len(sys.argv) > 1 else "demo"
client = Client()

# Watch which agent has focus and print a message when it changes
def watch_focus():
    was_focused = None
    for status in client.subscribe_status(reconnect=True):
        platform = status.platform or {}
        output = platform.get("output", {})
        is_focused = output.get("current_agent") == name

        if is_focused != was_focused:
            was_focused = is_focused
            print("[agent] Hey, I'm here!" if is_focused else "[agent] Ok, I'll wait here.")

threading.Thread(target=watch_focus, daemon=True).start()

# Listen for transcriptions and echo them back via TTS
try:
    for message in client.subscribe(name, reconnect=True):
        print(f"[user ] {message.text}")

        if message.text.strip():
            client.speak(f"You said: {message.text}", language="en")
except KeyboardInterrupt:
    print("\nStopped.")
