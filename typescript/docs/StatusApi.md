# StatusApi

All URIs are relative to *http://localhost:8770*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getStatus**](StatusApi.md#getstatus) | **GET** /status | Get engine status |



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

