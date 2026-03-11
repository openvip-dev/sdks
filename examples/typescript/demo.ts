// OpenVIP TypeScript SDK demo
// Usage: npx tsx demo.ts [NAME]

import { Client } from "../../typescript/src";

const name = process.argv[2] || "demo";
const client = new Client();

// Watch which agent has focus and print a message when it changes
(async () => {
  let wasFocused: boolean | null = null;
  for await (const status of client.subscribeStatus({ reconnect: true })) {
    const platform = (status as any).platform || {};
    const isFocused = platform.output?.current_agent === name;

    if (isFocused !== wasFocused) {
      wasFocused = isFocused;
      console.log(isFocused ? "[agent] Hey, I'm here!" : "[agent] Ok, I'll wait here.");
    }
  }
})();

// Listen for transcriptions and echo them back via TTS
(async () => {
  for await (const message of client.subscribe(name, { reconnect: true })) {
    console.log(`[user ] ${message.text}`);

    if (message.text?.trim()) {
      await client.speak(`You said: ${message.text}`, { language: "en" });
    }
  }
})();
