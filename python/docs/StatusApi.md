# openvip.StatusApi

All URIs are relative to *http://localhost:8770*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_status**](StatusApi.md#get_status) | **GET** /status | Get engine status


# **get_status**
> Status get_status()

Get engine status

Get the current status of the engine. Returns protocol-level information
(connected agents, protocol version) and implementation-specific details
in the `platform` object.


### Example


```python
import openvip
from openvip.models.status import Status
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
    api_instance = openvip.StatusApi(api_client)

    try:
        # Get engine status
        api_response = api_instance.get_status()
        print("The response of StatusApi->get_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusApi->get_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Status**](Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Engine status |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

