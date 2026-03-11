/**
 * Convenience factories for OpenVIP messages.
 *
 * @example
 * ```typescript
 * import { createTranscription, createSpeechRequest } from "openvip";
 *
 * const msg = createTranscription("hello world", { language: "en" });
 * const req = createSpeechRequest("hello world", "en");
 * ```
 */

import type { Transcription, SpeechRequest, ControlRequest } from "./models";
import {
  TranscriptionTypeEnum,
  SpeechRequestTypeEnum,
  ControlRequestOpenvipEnum,
  ControlRequestCommandEnum,
} from "./models";

export const PROTOCOL_VERSION = "1.0";

/**
 * Create a Transcription message with auto-filled protocol fields.
 *
 * Automatically generates `id` (UUID) and `timestamp` (now, UTC).
 */
export function createTranscription(
  text: string,
  options?: {
    language?: string;
    confidence?: number;
    partial?: boolean;
    origin?: string;
    traceId?: string;
    parentId?: string;
  },
): Transcription {
  return {
    openvip: PROTOCOL_VERSION,
    type: TranscriptionTypeEnum.Transcription,
    id: crypto.randomUUID(),
    timestamp: new Date(),
    text,
    ...options,
  };
}

/**
 * Create a SpeechRequest with auto-filled protocol fields.
 *
 * Automatically generates `id` (UUID) and `timestamp` (now, UTC).
 */
export function createSpeechRequest(
  text: string,
  language?: string,
): SpeechRequest {
  return {
    openvip: PROTOCOL_VERSION,
    type: SpeechRequestTypeEnum.Speech,
    id: crypto.randomUUID(),
    timestamp: new Date(),
    text,
    language,
  };
}

/**
 * Create a ControlRequest with auto-filled protocol fields.
 *
 * Automatically generates `id` (UUID).
 */
export function createControlRequest(
  command: string,
): ControlRequest {
  return {
    openvip: ControlRequestOpenvipEnum._10,
    id: crypto.randomUUID(),
    command: command as ControlRequestCommandEnum,
  };
}
