/**
 * OpenVIP TypeScript SDK demo.
 *
 * Connects to a local OpenVIP engine (e.g. VoxType) and demonstrates
 * SDK features: status, control, speech, and messaging.
 *
 * Usage:
 *   cd ../../typescript && npm install && cd ../examples/typescript
 *   npx ts-node demo.ts
 */

import {
  Configuration,
  ControlApi,
  MessagesApi,
  SpeechApi,
  StatusApi,
} from "../../typescript/src";

const BASE_URL = process.argv[2] || "http://localhost:8770";

async function main() {
  const config = new Configuration({ basePath: BASE_URL });

  const statusApi = new StatusApi(config);
  const controlApi = new ControlApi(config);
  const speechApi = new SpeechApi(config);
  const messagesApi = new MessagesApi(config);

  console.log("OpenVIP TypeScript SDK demo");
  console.log(`Connecting to ${BASE_URL}...`);
  console.log();

  // 1. Status
  console.log("=== GET /status ===");
  try {
    const status = await statusApi.getStatus();
    console.log(`  Protocol: ${status.protocolVersion}`);
    console.log(`  Agents:   ${JSON.stringify(status.connectedAgents)}`);
  } catch (e: any) {
    console.log(`  Error: ${e.message}`);
    console.log(
      "  Is the engine running? Start VoxType with: voxtype listen --agents"
    );
    process.exit(1);
  }
  console.log();

  // 2. Control — start listening
  console.log("=== POST /control (stt.start) ===");
  try {
    const ack = await controlApi.sendControl({ command: "stt.start" });
    console.log(`  Response: ${ack.status}`);
  } catch (e: any) {
    console.log(`  Error: ${e.message}`);
  }
  console.log();

  // 3. Speech — text-to-speech
  console.log("=== POST /speech ===");
  try {
    const resp = await speechApi.textToSpeech({
      openvip: "1.0",
      type: "speech",
      text: "Hello from the OpenVIP TypeScript SDK!",
      language: "en",
    });
    console.log(`  Status:   ${resp.status}`);
    console.log(`  Duration: ${resp.durationMs}ms`);
  } catch (e: any) {
    console.log(`  Error: ${e.message}`);
  }
  console.log();

  // 4. Send message
  console.log("=== POST /agents/demo/messages ===");
  try {
    const ack = await messagesApi.sendMessage({
      agentId: "demo",
      transcription: {
        openvip: "1.0",
        type: "transcription",
        id: crypto.randomUUID(),
        timestamp: new Date(),
        text: "Test message from TypeScript SDK demo",
        language: "en",
      },
    });
    console.log(`  Response: ${ack.status}`);
  } catch (e: any) {
    console.log(`  Error: ${e.message} (expected if no 'demo' agent connected)`);
  }
  console.log();

  // 5. Control — stop listening
  console.log("=== POST /control (stt.stop) ===");
  try {
    const ack = await controlApi.sendControl({ command: "stt.stop" });
    console.log(`  Response: ${ack.status}`);
  } catch (e: any) {
    console.log(`  Error: ${e.message}`);
  }
  console.log();

  console.log("Demo complete!");
}

main().catch(console.error);
