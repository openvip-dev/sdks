# OpenVip.Api.StatusApi

All URIs are relative to *http://localhost:8770/openvip*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**GetStatus**](StatusApi.md#getstatus) | **GET** /status | Get engine status |
| [**SubscribeStatus**](StatusApi.md#subscribestatus) | **GET** /status/stream | Subscribe to status changes (SSE) |

<a id="getstatus"></a>
# **GetStatus**
> Status GetStatus ()

Get engine status

Get the current status of the engine. Returns protocol-level information (connected agents, protocol version) and implementation-specific details in the `platform` object. 


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
| **200** | Engine status |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="subscribestatus"></a>
# **SubscribeStatus**
> string SubscribeStatus ()

Subscribe to status changes (SSE)

Server-Sent Events stream that pushes status updates on state transitions.  Events are sent when `stt`, `tts`, `connected_agents`, or other discrete fields change. Continuously changing fields (e.g., `uptime_seconds`) do not trigger events.  The payload of each event is a `Status` object — the same schema as the `GET /status` response.  Keepalive comments (`: keepalive`) are sent every 30 seconds if no events occur.  Clients that cannot use SSE should fall back to polling `GET /status`. 


### Parameters
This endpoint does not need any parameter.
### Return type

**string**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/event-stream


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | SSE stream established |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

