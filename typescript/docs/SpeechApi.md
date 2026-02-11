# SpeechApi

All URIs are relative to *http://localhost:8770*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**textToSpeech**](SpeechApi.md#texttospeech) | **POST** /speech | Text-to-speech request |



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
    speechRequest: {"openvip":"1.0","type":"speech","text":"Light turned on","language":"en"},
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

