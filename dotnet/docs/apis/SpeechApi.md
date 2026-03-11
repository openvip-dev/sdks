# OpenVip.Api.SpeechApi

All URIs are relative to *http://localhost:8770/openvip*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**StopSpeech**](SpeechApi.md#stopspeech) | **POST** /speech/stop | Stop TTS playback |
| [**TextToSpeech**](SpeechApi.md#texttospeech) | **POST** /speech | Text-to-speech request |

<a id="stopspeech"></a>
# **StopSpeech**
> Response StopSpeech ()

Stop TTS playback

Interrupt the currently playing TTS audio immediately. If no audio is playing, the request is a no-op (still returns 200). 


### Parameters
This endpoint does not need any parameter.
### Return type

[**Response**](Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Stop request delivered (audio may already be finished) |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="texttospeech"></a>
# **TextToSpeech**
> SpeechResponse TextToSpeech (SpeechRequest speechRequest)

Text-to-speech request

Request text-to-speech synthesis. The engine will speak the provided text. 


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **speechRequest** | [**SpeechRequest**](SpeechRequest.md) |  |  |

### Return type

[**SpeechResponse**](SpeechResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Speech synthesis completed |  -  |
| **400** | Invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

