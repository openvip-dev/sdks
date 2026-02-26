# openvip.SpeechApi

All URIs are relative to *http://localhost:8770*

Method | HTTP request | Description
------------- | ------------- | -------------
[**text_to_speech**](SpeechApi.md#text_to_speech) | **POST** /speech | Text-to-speech request


# **text_to_speech**
> SpeechResponse text_to_speech(speech_request)

Text-to-speech request

Request text-to-speech synthesis. The engine will speak the provided text.


### Example


```python
import openvip
from openvip.models.speech_request import SpeechRequest
from openvip.models.speech_response import SpeechResponse
from openvip.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8770
# See configuration.py for a list of all supported configuration parameters.
configuration = openvip.Configuration(
    host = "http://localhost:8770"
)


# Enter a context with an instance of the API client
with openvip.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openvip.SpeechApi(api_client)
    speech_request = {"openvip":"1.0","type":"speech","id":"660e8400-e29b-41d4-a716-446655440001","timestamp":"2026-02-06T10:30:05Z","text":"Light turned on","language":"en"} # SpeechRequest | 

    try:
        # Text-to-speech request
        api_response = api_instance.text_to_speech(speech_request)
        print("The response of SpeechApi->text_to_speech:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpeechApi->text_to_speech: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **speech_request** | [**SpeechRequest**](SpeechRequest.md)|  | 

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
**200** | Speech synthesis completed |  -  |
**400** | Invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

