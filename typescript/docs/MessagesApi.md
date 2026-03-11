# MessagesApi

All URIs are relative to *http://localhost:8770/openvip*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sendMessage**](MessagesApi.md#sendmessage) | **POST** /agents/{agent_id}/messages | Send message to agent |
| [**subscribeAgent**](MessagesApi.md#subscribeagent) | **GET** /agents/{agent_id}/messages | Subscribe to agent messages (SSE) |



## sendMessage

> Response sendMessage(agentId, message)

Send message to agent

Send a voice interaction message to a specific agent. The agent must be connected via SSE (GET endpoint) to receive messages. 

### Example

```ts
import {
  Configuration,
  MessagesApi,
} from 'openvip';
import type { SendMessageRequest } from 'openvip';

async function example() {
  console.log("🚀 Testing openvip SDK...");
  const api = new MessagesApi();

  const body = {
    // string | Agent identifier
    agentId: agentId_example,
    // Message
    message: {"openvip":"1.0","type":"transcription","id":"550e8400-e29b-41d4-a716-446655440000","timestamp":"2026-02-06T10:30:00Z","text":"turn on the light","language":"en"},
  } satisfies SendMessageRequest;

  try {
    const data = await api.sendMessage(body);
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
| **agentId** | `string` | Agent identifier | [Defaults to `undefined`] |
| **message** | [Message](Message.md) |  | |

### Return type

[**Response**](Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Message delivered |  -  |
| **400** | Invalid message format |  -  |
| **404** | Agent not connected |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## subscribeAgent

> string subscribeAgent(agentId)

Subscribe to agent messages (SSE)

Server-Sent Events stream for messages to this agent.  The SSE connection acts as agent registration — the agent exists as long as this connection is open. When the client disconnects, the agent is automatically de-registered.  Reconnect on disconnect. Messages sent while disconnected are lost (ephemeral model).  Keepalive comments (&#x60;: keepalive&#x60;) are sent every 30 seconds if no data. 

### Example

```ts
import {
  Configuration,
  MessagesApi,
} from 'openvip';
import type { SubscribeAgentRequest } from 'openvip';

async function example() {
  console.log("🚀 Testing openvip SDK...");
  const api = new MessagesApi();

  const body = {
    // string | Agent identifier
    agentId: agentId_example,
  } satisfies SubscribeAgentRequest;

  try {
    const data = await api.subscribeAgent(body);
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
| **agentId** | `string` | Agent identifier | [Defaults to `undefined`] |

### Return type

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `text/event-stream`, `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | SSE stream established |  -  |
| **409** | Agent ID already connected |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

