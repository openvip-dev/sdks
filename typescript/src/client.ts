/**
 * High-level OpenVIP client for TypeScript.
 *
 * @example
 * ```typescript
 * import { Client, createTranscription } from "openvip";
 *
 * const client = new Client("http://localhost:8770/openvip");
 * await client.speak("Hello world", { language: "en" });
 * const status = await client.getStatus();
 *
 * // Subscribe to messages (async iterator)
 * for await (const msg of client.subscribe("my-agent", { reconnect: true })) {
 *   console.log(msg.text);
 * }
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
  Response as ResponseMessage,
  Transcription,
  SpeechRequest,
} from "./models";
import {
  ControlRequestOpenvipEnum,
  ControlRequestCommandEnum,
  TranscriptionFromJSON,
  SpeechRequestFromJSON,
  StatusFromJSON,
} from "./models";

const DEFAULT_URL = "http://localhost:8770/openvip";

export class DuplicateAgentError extends Error {
  constructor(message: string) {
    super(message);
    this.name = "DuplicateAgentError";
  }
}

export interface SubscribeOptions {
  /** Auto-reconnect on connection loss (default: false). */
  reconnect?: boolean;
  /** Initial delay between reconnection attempts in seconds (default: 0.5). */
  retryDelay?: number;
  /** Maximum delay between reconnection attempts in seconds (default: 5). */
  maxRetryDelay?: number;
  /** AbortSignal to stop the subscription. */
  signal?: AbortSignal;
  /** Called on each successful connection. */
  onConnect?: () => void;
  /** Called on disconnection, receives the error (or undefined for clean disconnect). */
  onDisconnect?: (error?: Error) => void;
}

export class Client {
  private url: string;
  private statusApi: StatusApi;
  private speechApi: SpeechApi;
  private controlApi: ControlApi;
  private messagesApi: MessagesApi;

  constructor(url: string = DEFAULT_URL) {
    this.url = url.replace(/\/$/, "");
    const config = new Configuration({ basePath: this.url });
    this.statusApi = new StatusApi(config);
    this.speechApi = new SpeechApi(config);
    this.controlApi = new ControlApi(config);
    this.messagesApi = new MessagesApi(config);
  }

  // --- Speech ---

  /** Request text-to-speech synthesis. */
  async speak(
    text: string,
    options?: { language?: string },
  ): Promise<SpeechResponse> {
    const req = createSpeechRequest(text, options?.language);
    return this.speechApi.textToSpeech({ speechRequest: req });
  }

  // --- Status ---

  /** Get engine status. */
  async getStatus(): Promise<Status> {
    return this.statusApi.getStatus();
  }

  /** Check if the engine is reachable. */
  async isAvailable(): Promise<boolean> {
    try {
      await this.getStatus();
      return true;
    } catch {
      return false;
    }
  }

  // --- Control ---

  /** Send a control command. */
  async control(command: string): Promise<ResponseMessage> {
    return this.controlApi.sendControl({
      controlRequest: {
        openvip: ControlRequestOpenvipEnum._10,
        id: crypto.randomUUID(),
        command: command as ControlRequestCommandEnum,
      },
    });
  }

  /** Start speech-to-text. */
  async startListening(): Promise<ResponseMessage> {
    return this.control("stt.start");
  }

  /** Stop speech-to-text. */
  async stopListening(): Promise<ResponseMessage> {
    return this.control("stt.stop");
  }

  /** Request engine shutdown. */
  async shutdown(): Promise<ResponseMessage> {
    return this.control("engine.shutdown");
  }

  // --- Messages ---

  /** Send a message to a connected agent. */
  async sendMessage(agentId: string, message: Transcription): Promise<ResponseMessage> {
    return this.messagesApi.sendMessage({
      agentId,
      message,
    });
  }

  /**
   * Subscribe to messages for an agent via SSE.
   *
   * The SSE connection acts as agent registration — the agent exists
   * as long as the iteration is active.
   *
   * @example
   * ```typescript
   * const controller = new AbortController();
   * for await (const msg of client.subscribe("my-agent", {
   *   reconnect: true,
   *   signal: controller.signal,
   * })) {
   *   if (msg.type === "transcription") {
   *     console.log(msg.text);
   *   }
   * }
   * ```
   */
  async *subscribe(
    agentId: string,
    options?: SubscribeOptions,
  ): AsyncIterableIterator<Transcription | SpeechRequest> {
    const url = `${this.url}/agents/${encodeURIComponent(agentId)}/messages`;
    yield* this.sseStream(url, parseAgentMessage, options, {
      conflictMessage: `Agent '${agentId}' is already connected`,
    });
  }

  /**
   * Subscribe to status changes via SSE.
   *
   * Events are sent only on state transitions (e.g. idle → listening,
   * agent connect/disconnect).
   */
  async *subscribeStatus(
    options?: SubscribeOptions,
  ): AsyncIterableIterator<Status> {
    const url = `${this.url}/status/stream`;
    yield* this.sseStream(url, (data) => StatusFromJSON(data), options);
  }

  // --- SSE helper ---

  private async *sseStream<T>(
    url: string,
    parse: (data: Record<string, unknown>) => T,
    options?: SubscribeOptions,
    extra?: { conflictMessage?: string },
  ): AsyncIterableIterator<T> {
    const reconnect = options?.reconnect ?? false;
    const retryDelay = options?.retryDelay ?? 0.5;
    const maxRetryDelay = options?.maxRetryDelay ?? 5;
    let currentDelay = retryDelay;

    while (true) {
      try {
        const response = await fetch(url, {
          headers: { Accept: "text/event-stream" },
          signal: options?.signal,
        });

        if (response.status === 409) {
          throw new DuplicateAgentError(
            extra?.conflictMessage ?? `SSE conflict (409) for ${url}`,
          );
        }
        if (!response.ok) {
          throw new Error(`SSE connection failed: ${response.status}`);
        }

        currentDelay = retryDelay;
        options?.onConnect?.();

        const reader = response.body?.getReader();
        if (!reader) throw new Error("No response body");

        const decoder = new TextDecoder();
        let buffer = "";

        try {
          while (true) {
            const { done, value } = await reader.read();
            if (done) break;

            buffer += decoder.decode(value, { stream: true });
            const lines = buffer.split("\n");
            buffer = lines.pop() ?? "";

            let eventData = "";
            for (let line of lines) {
              line = line.replace(/\r$/, "");
              if (line.startsWith("data: ")) {
                eventData += line.slice(6);
              } else if (line === "" && eventData) {
                try {
                  const data = JSON.parse(eventData);
                  yield parse(data);
                } catch {
                  // Ignore malformed events
                }
                eventData = "";
              }
            }
          }
        } finally {
          reader.releaseLock();
        }

        // Stream ended cleanly
        options?.onDisconnect?.();
        if (!reconnect) return;

      } catch (err: unknown) {
        if (err instanceof DuplicateAgentError) throw err;
        if (err instanceof Error && err.name === "AbortError") return;

        options?.onDisconnect?.(err instanceof Error ? err : undefined);
        if (!reconnect) throw err;
      }

      // Reconnect with backoff
      if (options?.signal?.aborted) return;
      await new Promise((r) => setTimeout(r, currentDelay * 1000));
      currentDelay = Math.min(currentDelay * 2, maxRetryDelay);
    }
  }
}

// --- Message parsing ---

function parseAgentMessage(
  data: Record<string, unknown>,
): Transcription | SpeechRequest {
  if (data.type === "speech") {
    return SpeechRequestFromJSON(data);
  }
  return TranscriptionFromJSON(data);
}
