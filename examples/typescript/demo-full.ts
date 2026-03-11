#!/usr/bin/env npx tsx
/**
 * OpenVIP TypeScript SDK — minimal voice agent demo.
 *
 * Subscribes as an agent, prints transcriptions, and echoes them back via TTS.
 * Press Ctrl+C to stop.
 *
 * Usage:
 *   npm install openvip
 *   npx tsx demo.ts [URL]
 */

import { Client, DuplicateAgentError } from "../../typescript/src";

const url = process.argv[2] || "http://localhost:8770/openvip";
const client = new Client(url);

if (!(await client.isAvailable())) {
  console.log(`Engine not available at ${url}`);
  process.exit(1);
}

const status = await client.getStatus();
console.log(`Connected — agents: ${status.connectedAgents}`);
console.log("Listening for voice... (Ctrl+C to stop)\n");

const controller = new AbortController();
process.on("SIGINT", () => {
  console.log("\nStopped.");
  controller.abort();
});

try {
  for await (const msg of client.subscribe("demo", {
    reconnect: true,
    signal: controller.signal,
  })) {
    console.log(`[${msg.type}] ${msg.text}`);
    if (msg.text?.trim()) {
      await client.speak(`You said: ${msg.text}`, { language: "en" });
    }
  }
} catch (err) {
  if (err instanceof DuplicateAgentError) {
    console.log("Agent 'demo' is already connected.");
  } else if (!(err instanceof Error && err.name === "AbortError")) {
    throw err;
  }
}
