# openvip.MessagesApi

All URIs are relative to *http://localhost:8770*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_message**](MessagesApi.md#send_message) | **POST** /agents/{agent_id}/messages | Send message to agent
[**subscribe_agent**](MessagesApi.md#subscribe_agent) | **GET** /agents/{agent_id}/messages | Subscribe to agent messages (SSE)


# **send_message**
> Response send_message(agent_id, message)

Send message to agent

Send a voice interaction message to a specific agent.
The agent must be connected via SSE (GET endpoint) to receive messages.


### Example


```python
import openvip
from openvip.models.message import Message
from openvip.models.response import Response
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
    api_instance = openvip.MessagesApi(api_client)
    agent_id = 'agent_id_example' # str | Agent identifier
    message = {"openvip":"1.0","type":"transcription","id":"550e8400-e29b-41d4-a716-446655440000","timestamp":"2026-02-06T10:30:00Z","text":"turn on the light","language":"en"} # Message | 

    try:
        # Send message to agent
        api_response = api_instance.send_message(agent_id, message)
        print("The response of MessagesApi->send_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->send_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**| Agent identifier | 
 **message** | [**Message**](Message.md)|  | 

### Return type

[**Response**](Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Message delivered |  -  |
**400** | Invalid message format |  -  |
**404** | Agent not connected |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscribe_agent**
> str subscribe_agent(agent_id)

Subscribe to agent messages (SSE)

Server-Sent Events stream for messages to this agent.

The SSE connection acts as agent registration — the agent exists
as long as this connection is open. When the client disconnects,
the agent is automatically de-registered.

Reconnect on disconnect. Messages sent while disconnected are lost
(ephemeral model).

Keepalive comments (`: keepalive`) are sent every 30 seconds if no data.


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
    api_instance = openvip.MessagesApi(api_client)
    agent_id = 'agent_id_example' # str | Agent identifier

    try:
        # Subscribe to agent messages (SSE)
        api_response = api_instance.subscribe_agent(agent_id)
        print("The response of MessagesApi->subscribe_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->subscribe_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**| Agent identifier | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/event-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SSE stream established |  -  |
**409** | Agent ID already connected |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

