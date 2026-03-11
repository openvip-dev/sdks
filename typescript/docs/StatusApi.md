# StatusApi

All URIs are relative to *http://localhost:8770/openvip*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getStatus**](StatusApi.md#getstatus) | **GET** /status | Get engine status |
| [**subscribeStatus**](StatusApi.md#subscribestatus) | **GET** /status/stream | Subscribe to status changes (SSE) |



## getStatus

> Status getStatus()

Get engine status

Get the current status of the engine. Returns protocol-level information (connected agents, protocol version) and implementation-specific details in the &#x60;platform&#x60; object. 

### Example

```ts
import {
  Configuration,
  StatusApi,
} from 'openvip';
import type { GetStatusRequest } from 'openvip';

async function example() {
  console.log("🚀 Testing openvip SDK...");
  const api = new StatusApi();

  try {
    const data = await api.getStatus();
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

[**Status**](Status.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Engine status |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## subscribeStatus

> string subscribeStatus()

Subscribe to status changes (SSE)

Server-Sent Events stream that pushes status updates on state transitions.  Events are sent when &#x60;stt&#x60;, &#x60;tts&#x60;, &#x60;connected_agents&#x60;, or other discrete fields change. Continuously changing fields (e.g., &#x60;uptime_seconds&#x60;) do not trigger events.  The payload of each event is a &#x60;Status&#x60; object — the same schema as the &#x60;GET /status&#x60; response.  Keepalive comments (&#x60;: keepalive&#x60;) are sent every 30 seconds if no events occur.  Clients that cannot use SSE should fall back to polling &#x60;GET /status&#x60;. 

### Example

```ts
import {
  Configuration,
  StatusApi,
} from 'openvip';
import type { SubscribeStatusRequest } from 'openvip';

async function example() {
  console.log("🚀 Testing openvip SDK...");
  const api = new StatusApi();

  try {
    const data = await api.subscribeStatus();
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

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `text/event-stream`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | SSE stream established |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

