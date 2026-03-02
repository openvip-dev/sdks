# openvip.StatusApi

All URIs are relative to *http://localhost:8770*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_status**](StatusApi.md#get_status) | **GET** /status | Get engine status
[**subscribe_status**](StatusApi.md#subscribe_status) | **GET** /status/stream | Subscribe to status changes (SSE)


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

# **subscribe_status**
> str subscribe_status()

Subscribe to status changes (SSE)

Server-Sent Events stream that pushes status updates on state transitions.

Events are sent when `stt`, `tts`, `connected_agents`, or other
discrete fields change. Continuously changing fields (e.g.,
`uptime_seconds`) do not trigger events.

The payload of each event is a `Status` object — the same schema as
the `GET /status` response.

Keepalive comments (`: keepalive`) are sent every 30 seconds if no
events occur.

Clients that cannot use SSE should fall back to polling `GET /status`.


### Example


```python
import openvip
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
        # Subscribe to status changes (SSE)
        api_response = api_instance.subscribe_status()
        print("The response of StatusApi->subscribe_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusApi->subscribe_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/event-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SSE stream established |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

