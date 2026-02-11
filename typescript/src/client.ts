/**
 * High-level OpenVIP client for TypeScript.
 *
 * @example
 * ```typescript
 * import { Client, createTranscription } from "openvip";
 *
 * const client = new Client("http://localhost:8770");
 * await client.speak("Hello world", { language: "en" });
 * const status = await client.getStatus();
 * await client.startListening();
 *
 * const msg = createTranscription("turn on the light", { language: "en" });
 * await client.sendMessage("my-agent", msg);
 * ```
 */

import { Configuration } from "./runtime";
import { StatusApi } from "./apis/StatusApi";
import { SpeechApi } from "./apis/SpeechApi";
import { ControlApi } from "./apis/ControlApi";
import { MessagesApi } from "./apis/MessagesApi";
import { createSpeechRequest } from "./messages";
import type {
  Status,
  SpeechResponse,
  Ack,
  Transcription,
  ControlRequestCommandEnum,
} from "./models";

const DEFAULT_URL = "http://localhost:8770";

export class Client {
  private statusApi: StatusApi;
  private speechApi: SpeechApi;
  private controlApi: ControlApi;
  private messagesApi: MessagesApi;

  constructor(url: string = DEFAULT_URL) {
    const config = new Configuration({ basePath: url });
    this.statusApi = new StatusApi(config);
    this.speechApi = new SpeechApi(config);
    this.controlApi = new ControlApi(config);
    this.messagesApi = new MessagesApi(config);
  }

  /** Request text-to-speech synthesis. */
  async speak(
    text: string,
    options?: { language?: string },
  ): Promise<SpeechResponse> {
    const req = createSpeechRequest(text, options?.language);
    return this.speechApi.textToSpeech({ speechRequest: req });
  }

  /** Get engine status. */
  async getStatus(): Promise<Status> {
    return this.statusApi.getStatus();
  }

  /** Send a control command. */
  async control(command: ControlRequestCommandEnum): Promise<Ack> {
    return this.controlApi.sendControl({
      controlRequest: { command },
    });
  }

  /** Start speech-to-text. */
  async startListening(): Promise<Ack> {
    return this.control("stt.start");
  }

  /** Stop speech-to-text. */
  async stopListening(): Promise<Ack> {
    return this.control("stt.stop");
  }

  /** Request engine shutdown. */
  async shutdown(): Promise<Ack> {
    return this.control("engine.shutdown");
  }

  /** Send a message to a connected agent. */
  async sendMessage(agentId: string, message: Transcription): Promise<Ack> {
    return this.messagesApi.sendMessage({
      agentId,
      transcription: message,
    });
  }
}
