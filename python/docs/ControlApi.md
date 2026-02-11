# openvip.ControlApi

All URIs are relative to *http://localhost:8770*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_control**](ControlApi.md#send_control) | **POST** /control | Send control command


# **send_control**
> Ack send_control(control_request)

Send control command

Send a control command to the engine.

Available commands:
- `stt.start` — Start speech-to-text
- `stt.stop` — Stop speech-to-text
- `engine.shutdown` — Graceful shutdown


### Example


```python
import openvip
from openvip.models.ack import Ack
from openvip.models.control_request import ControlRequest
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
    api_instance = openvip.ControlApi(api_client)
    control_request = {"command":"stt.stop"} # ControlRequest | 

    try:
        # Send control command
        api_response = api_instance.send_control(control_request)
        print("The response of ControlApi->send_control:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ControlApi->send_control: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **control_request** | [**ControlRequest**](ControlRequest.md)|  | 

### Return type

[**Ack**](Ack.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Command executed |  -  |
**400** | Invalid command |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

