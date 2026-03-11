/**
 * Tests for hand-written Client wrapper.
 * Mirrors Python SDK tests in tests/test_client.py.
 */

import { describe, it, expect, vi, beforeEach } from "vitest";
import { Client, DuplicateAgentError } from "../src/client";
import { PROTOCOL_VERSION } from "../src/messages";

// --- Helpers ---

/** Create a mock fetch Response with JSON body. */
function mockJsonResponse(data: Record<string, unknown>, status = 200): Response {
  return new Response(JSON.stringify(data), {
    status,
    headers: { "Content-Type": "application/json" },
  });
}

/** Create a mock SSE stream response. */
function mockSSEResponse(lines: string[]): Response {
  const text = lines.join("");
  const encoder = new TextEncoder();
  const stream = new ReadableStream({
    start(controller) {
      controller.enqueue(encoder.encode(text));
      controller.close();
    },
  });
  return new Response(stream, {
    status: 200,
    headers: { "Content-Type": "text/event-stream" },
  });
}

/** Build an SSE transcription event. */
function sseTranscription(text: string, id = "550e8400-e29b-41d4-a716-446655440000"): string {
  const data = JSON.stringify({
    openvip: "1.0",
    type: "transcription",
    id,
    timestamp: "2026-01-01T00:00:00Z",
    text,
  });
  return `event: transcription\r\ndata: ${data}\r\n\r\n`;
}

// --- Tests ---

describe("Client init", () => {
  it("uses default URL", () => {
    const c = new Client();
    expect((c as any).url).toBe("http://localhost:8770/openvip");
  });

  it("accepts custom URL", () => {
    const c = new Client("http://myhost:9999");
    expect((c as any).url).toBe("http://myhost:9999");
  });

  it("strips trailing slash", () => {
    const c = new Client("http://myhost:9999/");
    expect((c as any).url).toBe("http://myhost:9999");
  });

  it("accepts timeout option", () => {
    const c = new Client("http://myhost:9999", { timeout: 5 });
    expect((c as any).timeout).toBe(5000);
  });

  it("defaults timeout to 10s", () => {
    const c = new Client();
    expect((c as any).timeout).toBe(10000);
  });

  it("stores token", () => {
    const c = new Client("http://myhost:9999", { token: "my-secret" });
    expect((c as any).token).toBe("my-secret");
  });
});

describe("Client.getStatus", () => {
  beforeEach(() => { vi.restoreAllMocks(); });

  it("returns status", async () => {
    vi.spyOn(globalThis, "fetch").mockResolvedValue(
      mockJsonResponse({
        openvip: "1.0",
        connected_agents: ["claude", "shell"],
        platform: { state: "listening" },
      }),
    );
    const client = new Client("http://test:8770");
    const status = await client.getStatus();

    expect(status.connectedAgents).toEqual(["claude", "shell"]);
    expect(status.platform).toEqual({ state: "listening" });
  });
});

describe("Client.isAvailable", () => {
  beforeEach(() => { vi.restoreAllMocks(); });

  it("returns true when engine responds", async () => {
    vi.spyOn(globalThis, "fetch").mockResolvedValue(
      mockJsonResponse({ openvip: "1.0", connected_agents: [] }),
    );
    const client = new Client("http://test:8770");
    expect(await client.isAvailable()).toBe(true);
  });

  it("returns false when engine unreachable", async () => {
    vi.spyOn(globalThis, "fetch").mockRejectedValue(new Error("ECONNREFUSED"));
    const client = new Client("http://test:8770");
    expect(await client.isAvailable()).toBe(false);
  });
});

describe("Client.control", () => {
  beforeEach(() => { vi.restoreAllMocks(); });

  it("sends control command", async () => {
    const fetchSpy = vi.spyOn(globalThis, "fetch").mockResolvedValue(
      mockJsonResponse({ openvip: "1.0", status: "ok" }),
    );
    const client = new Client("http://test:8770");
    await client.control("stt.toggle");

    const [url, opts] = fetchSpy.mock.calls[0];
    expect(url).toContain("/control");
    const body = JSON.parse((opts as any).body);
    expect(body.command).toBe("stt.toggle");
  });

  it("startListening sends stt.start", async () => {
    const fetchSpy = vi.spyOn(globalThis, "fetch").mockResolvedValue(
      mockJsonResponse({ openvip: "1.0", status: "ok" }),
    );
    const client = new Client("http://test:8770");
    await client.startListening();

    const body = JSON.parse((fetchSpy.mock.calls[0][1] as any).body);
    expect(body.command).toBe("stt.start");
  });

  it("stopListening sends stt.stop", async () => {
    const fetchSpy = vi.spyOn(globalThis, "fetch").mockResolvedValue(
      mockJsonResponse({ openvip: "1.0", status: "ok" }),
    );
    const client = new Client("http://test:8770");
    await client.stopListening();

    const body = JSON.parse((fetchSpy.mock.calls[0][1] as any).body);
    expect(body.command).toBe("stt.stop");
  });
});

describe("Client.stopSpeech", () => {
  beforeEach(() => { vi.restoreAllMocks(); });

  it("sends POST to /speech/stop", async () => {
    const fetchSpy = vi.spyOn(globalThis, "fetch").mockResolvedValue(
      mockJsonResponse({ openvip: "1.0", status: "ok" }),
    );
    const client = new Client("http://test:8770");
    await client.stopSpeech();

    const [url, opts] = fetchSpy.mock.calls[0];
    expect(url).toBe("http://test:8770/speech/stop");
    expect((opts as any).method).toBe("POST");
  });

  it("includes token in Authorization header", async () => {
    const fetchSpy = vi.spyOn(globalThis, "fetch").mockResolvedValue(
      mockJsonResponse({ openvip: "1.0", status: "ok" }),
    );
    const client = new Client("http://test:8770", { token: "secret-123" });
    await client.stopSpeech();

    const headers = (fetchSpy.mock.calls[0][1] as any).headers;
    expect(headers.Authorization).toBe("Bearer secret-123");
  });
});

describe("Client.subscribe", () => {
  beforeEach(() => { vi.restoreAllMocks(); });

  it("yields transcriptions", async () => {
    vi.spyOn(globalThis, "fetch").mockResolvedValue(
      mockSSEResponse([
        sseTranscription("hello", "id-1"),
        sseTranscription("world", "id-2"),
      ]),
    );

    const client = new Client("http://test:8770");
    const messages = [];
    for await (const msg of client.subscribe("my-agent")) {
      messages.push(msg);
    }

    expect(messages).toHaveLength(2);
    expect(messages[0].text).toBe("hello");
    expect(messages[1].text).toBe("world");
  });

  it("skips bad JSON", async () => {
    vi.spyOn(globalThis, "fetch").mockResolvedValue(
      mockSSEResponse([
        "data: not-json\r\n\r\n",
        sseTranscription("ok"),
      ]),
    );

    const client = new Client("http://test:8770");
    const messages = [];
    for await (const msg of client.subscribe("my-agent")) {
      messages.push(msg);
    }

    expect(messages).toHaveLength(1);
    expect(messages[0].text).toBe("ok");
  });

  it("raises DuplicateAgentError on 409", async () => {
    vi.spyOn(globalThis, "fetch").mockResolvedValue(
      new Response("Conflict", { status: 409 }),
    );

    const client = new Client("http://test:8770");
    await expect(async () => {
      for await (const _ of client.subscribe("my-agent")) {
        // should not reach here
      }
    }).rejects.toThrow(DuplicateAgentError);
  });

  it("calls onConnect callback", async () => {
    vi.spyOn(globalThis, "fetch").mockResolvedValue(
      mockSSEResponse([sseTranscription("hi")]),
    );

    const onConnect = vi.fn();
    const client = new Client("http://test:8770");
    for await (const _ of client.subscribe("my-agent", { onConnect })) {
      // consume
    }

    expect(onConnect).toHaveBeenCalledOnce();
  });

  it("calls onDisconnect on clean close", async () => {
    vi.spyOn(globalThis, "fetch").mockResolvedValue(
      mockSSEResponse([]),  // empty stream
    );

    const onDisconnect = vi.fn();
    const client = new Client("http://test:8770");
    for await (const _ of client.subscribe("my-agent", { onDisconnect })) {
      // consume
    }

    expect(onDisconnect).toHaveBeenCalledOnce();
    expect(onDisconnect).toHaveBeenCalledWith();  // no error arg
  });

  it("reconnects on connection error", async () => {
    const controller = new AbortController();
    const fetchSpy = vi.spyOn(globalThis, "fetch")
      .mockRejectedValueOnce(new Error("ECONNREFUSED"))
      .mockResolvedValueOnce(mockSSEResponse([sseTranscription("recovered")]));

    // Mock setTimeout to avoid real delays
    vi.spyOn(globalThis, "setTimeout").mockImplementation((fn: any) => {
      fn();
      return 0 as any;
    });

    const client = new Client("http://test:8770");
    const messages = [];
    for await (const msg of client.subscribe("my-agent", {
      reconnect: true,
      signal: controller.signal,
    })) {
      messages.push(msg);
      controller.abort();  // stop after first message
    }

    expect(messages).toHaveLength(1);
    expect(messages[0].text).toBe("recovered");
    expect(fetchSpy).toHaveBeenCalledTimes(2);
    vi.restoreAllMocks();
  });

  it("reconnects with exponential backoff", async () => {
    const controller = new AbortController();
    vi.spyOn(globalThis, "fetch")
      .mockRejectedValueOnce(new Error("refused"))
      .mockRejectedValueOnce(new Error("refused"))
      .mockRejectedValueOnce(new Error("refused"))
      .mockResolvedValueOnce(mockSSEResponse([sseTranscription("ok")]));

    const delays: number[] = [];
    vi.spyOn(globalThis, "setTimeout").mockImplementation((fn: any, ms?: number) => {
      delays.push((ms ?? 0) / 1000);  // convert ms to seconds
      fn();
      return 0 as any;
    });

    const client = new Client("http://test:8770");
    for await (const _ of client.subscribe("my-agent", {
      reconnect: true,
      signal: controller.signal,
    })) {
      controller.abort();  // stop after first message
    }

    expect(delays).toEqual([0.5, 1.0, 2.0]);
    vi.restoreAllMocks();
  });

  it("caps reconnect delay at maxRetryDelay", async () => {
    const controller = new AbortController();
    vi.spyOn(globalThis, "fetch")
      .mockRejectedValueOnce(new Error("refused"))
      .mockRejectedValueOnce(new Error("refused"))
      .mockRejectedValueOnce(new Error("refused"))
      .mockRejectedValueOnce(new Error("refused"))
      .mockRejectedValueOnce(new Error("refused"))
      .mockResolvedValueOnce(mockSSEResponse([sseTranscription("ok")]));

    const delays: number[] = [];
    vi.spyOn(globalThis, "setTimeout").mockImplementation((fn: any, ms?: number) => {
      delays.push((ms ?? 0) / 1000);
      fn();
      return 0 as any;
    });

    const client = new Client("http://test:8770");
    for await (const _ of client.subscribe("my-agent", {
      reconnect: true,
      maxRetryDelay: 2,
      signal: controller.signal,
    })) {
      controller.abort();  // stop after first message
    }

    // 0.5, 1.0, 2.0, 2.0, 2.0 (capped)
    expect(delays).toEqual([0.5, 1.0, 2.0, 2.0, 2.0]);
    vi.restoreAllMocks();
  });

  it("still raises DuplicateAgentError with reconnect", async () => {
    vi.spyOn(globalThis, "fetch").mockResolvedValue(
      new Response("Conflict", { status: 409 }),
    );

    const client = new Client("http://test:8770");
    await expect(async () => {
      for await (const _ of client.subscribe("my-agent", { reconnect: true })) {
        // should not reach here
      }
    }).rejects.toThrow(DuplicateAgentError);
  });

  it("stops on AbortSignal", async () => {
    const controller = new AbortController();
    let count = 0;

    // Stream that yields two messages with a delay
    const encoder = new TextEncoder();
    const stream = new ReadableStream({
      start(ctrl) {
        ctrl.enqueue(encoder.encode(sseTranscription("first")));
        ctrl.enqueue(encoder.encode(sseTranscription("second")));
        ctrl.close();
      },
    });
    vi.spyOn(globalThis, "fetch").mockResolvedValue(
      new Response(stream, { status: 200 }),
    );

    const client = new Client("http://test:8770");
    for await (const msg of client.subscribe("my-agent", { signal: controller.signal })) {
      count++;
      if (count === 1) controller.abort();
    }

    expect(count).toBe(1);
  });

  it("does not reconnect when reconnect is false", async () => {
    vi.spyOn(globalThis, "fetch").mockRejectedValue(new Error("ECONNREFUSED"));

    const client = new Client("http://test:8770");
    await expect(async () => {
      for await (const _ of client.subscribe("my-agent", { reconnect: false })) {
        // should not reach here
      }
    }).rejects.toThrow("ECONNREFUSED");
  });

  it("includes token in SSE request", async () => {
    const fetchSpy = vi.spyOn(globalThis, "fetch").mockResolvedValue(
      mockSSEResponse([sseTranscription("hi")]),
    );

    const client = new Client("http://test:8770", { token: "sse-token" });
    for await (const _ of client.subscribe("my-agent")) {
      // consume
    }

    const headers = (fetchSpy.mock.calls[0][1] as any).headers;
    expect(headers.Authorization).toBe("Bearer sse-token");
  });

  it("handles CRLF in SSE lines", async () => {
    vi.spyOn(globalThis, "fetch").mockResolvedValue(
      mockSSEResponse([
        `event: transcription\r\ndata: {"openvip":"1.0","type":"transcription","id":"1","timestamp":"2026-01-01T00:00:00Z","text":"crlf test"}\r\n\r\n`,
      ]),
    );

    const client = new Client("http://test:8770");
    const messages = [];
    for await (const msg of client.subscribe("my-agent")) {
      messages.push(msg);
    }

    expect(messages).toHaveLength(1);
    expect(messages[0].text).toBe("crlf test");
  });
});
