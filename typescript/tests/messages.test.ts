import { describe, it, expect } from "vitest";
import {
  createTranscription,
  createSpeechRequest,
  createControlRequest,
  PROTOCOL_VERSION,
} from "../src/messages";

describe("createTranscription", () => {
  it("sets text and protocol fields", () => {
    const msg = createTranscription("hello world");
    expect(msg.text).toBe("hello world");
    expect(msg.openvip).toBe(PROTOCOL_VERSION);
    expect(msg.type).toBe("transcription");
  });

  it("generates a non-empty string id", () => {
    const msg = createTranscription("test");
    expect(typeof msg.id).toBe("string");
    expect(msg.id.length).toBeGreaterThan(0);
  });

  it("generates a Date timestamp", () => {
    const msg = createTranscription("test");
    expect(msg.timestamp).toBeInstanceOf(Date);
  });

  it("accepts language option", () => {
    const msg = createTranscription("ciao", { language: "it" });
    expect(msg.language).toBe("it");
  });

  it("accepts confidence option", () => {
    const msg = createTranscription("test", { confidence: 0.95 });
    expect(msg.confidence).toBe(0.95);
  });
});

describe("createSpeechRequest", () => {
  it("sets text and protocol fields", () => {
    const req = createSpeechRequest("say this", "en");
    expect(req.text).toBe("say this");
    expect(req.openvip).toBe(PROTOCOL_VERSION);
    expect(req.type).toBe("speech");
  });

  it("generates a non-empty string id", () => {
    const req = createSpeechRequest("test");
    expect(typeof req.id).toBe("string");
    expect(req.id.length).toBeGreaterThan(0);
  });

  it("generates a Date timestamp", () => {
    const req = createSpeechRequest("test");
    expect(req.timestamp).toBeInstanceOf(Date);
  });

  it("passes language parameter", () => {
    const req = createSpeechRequest("test", "fr");
    expect(req.language).toBe("fr");
  });
});

describe("createControlRequest", () => {
  it("sets command and protocol fields", () => {
    const req = createControlRequest("stt.start");
    expect(req.command).toBe("stt.start");
    expect(req.openvip).toBe("1.0");
    expect(req.id).toBeTruthy();
  });

  it("generates unique IDs across calls", () => {
    const a = createControlRequest("stt.start");
    const b = createControlRequest("stt.start");
    expect(a.id).not.toBe(b.id);
  });
});
