# SpeechApi

All URIs are relative to *http://localhost:8770/openvip*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**stopSpeech**](SpeechApi.md#stopspeech) | **POST** /speech/stop | Stop TTS playback |
| [**textToSpeech**](SpeechApi.md#texttospeech) | **POST** /speech | Text-to-speech request |



## stopSpeech

> Response stopSpeech()

Stop TTS playback

Interrupt the currently playing TTS audio immediately. If no audio is playing, the request is a no-op (still returns 200). 

### Example

```ts
import {
  Configuration,
  SpeechApi,
} from 'openvip';
import type { StopSpeechRequest } from 'openvip';

async function example() {
  console.log("🚀 Testing openvip SDK...");
  const api = new SpeechApi();

  try {
    const data = await api.stopSpeech();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**Response**](Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Stop request delivered (audio may already be finished) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## textToSpeech

> SpeechResponse textToSpeech(speechRequest)

Text-to-speech request

Request text-to-speech synthesis. The engine will speak the provided text. 

### Example

```ts
import {
  Configuration,
  SpeechApi,
} from 'openvip';
import type { TextToSpeechRequest } from 'openvip';

async function example() {
  console.log("🚀 Testing openvip SDK...");
  const api = new SpeechApi();

  const body = {
    // SpeechRequest
    speechRequest: {"openvip":"1.0","type":"speech","id":"660e8400-e29b-41d4-a716-446655440001","timestamp":"2026-02-06T10:30:05Z","text":"Light turned on","language":"en"},
  } satisfies TextToSpeechRequest;

  try {
    const data = await api.textToSpeech(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **speechRequest** | [SpeechRequest](SpeechRequest.md) |  | |

### Return type

[**SpeechResponse**](SpeechResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Speech synthesis completed |  -  |
| **400** | Invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

