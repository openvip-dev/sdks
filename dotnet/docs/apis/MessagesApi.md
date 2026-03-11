# OpenVip.Api.MessagesApi

All URIs are relative to *http://localhost:8770/openvip*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**SendMessage**](MessagesApi.md#sendmessage) | **POST** /agents/{agent_id}/messages | Send message to agent |
| [**SubscribeAgent**](MessagesApi.md#subscribeagent) | **GET** /agents/{agent_id}/messages | Subscribe to agent messages (SSE) |

<a id="sendmessage"></a>
# **SendMessage**
> Response SendMessage (string agentId, Message message)

Send message to agent

Send a voice interaction message to a specific agent. The agent must be connected via SSE (GET endpoint) to receive messages. 


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **agentId** | **string** | Agent identifier |  |
| **message** | [**Message**](Message.md) |  |  |

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
| **200** | Message delivered |  -  |
| **400** | Invalid message format |  -  |
| **404** | Agent not connected |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="subscribeagent"></a>
# **SubscribeAgent**
> string SubscribeAgent (string agentId)

Subscribe to agent messages (SSE)

Server-Sent Events stream for messages to this agent.  The SSE connection acts as agent registration — the agent exists as long as this connection is open. When the client disconnects, the agent is automatically de-registered.  Reconnect on disconnect. Messages sent while disconnected are lost (ephemeral model).  Keepalive comments (`: keepalive`) are sent every 30 seconds if no data. 


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **agentId** | **string** | Agent identifier |  |

### Return type

**string**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/event-stream, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | SSE stream established |  -  |
| **409** | Agent ID already connected |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

