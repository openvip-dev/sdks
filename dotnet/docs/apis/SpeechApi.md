# OpenVip.Api.SpeechApi

All URIs are relative to *http://localhost:8770*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**TextToSpeech**](SpeechApi.md#texttospeech) | **POST** /speech | Text-to-speech request |

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

