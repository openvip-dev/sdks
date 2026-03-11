# ControlApi

All URIs are relative to *http://localhost:8770/openvip*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sendControl**](ControlApi.md#sendcontrol) | **POST** /control | Send control command |



## sendControl

> Response sendControl(controlRequest)

Send control command

Send a control command to the engine.  Available commands: - &#x60;stt.start&#x60; — Start speech-to-text - &#x60;stt.stop&#x60; — Stop speech-to-text - &#x60;engine.shutdown&#x60; — Graceful shutdown 

### Example

```ts
import {
  Configuration,
  ControlApi,
} from 'openvip';
import type { SendControlRequest } from 'openvip';

async function example() {
  console.log("🚀 Testing openvip SDK...");
  const api = new ControlApi();

  const body = {
    // ControlRequest
    controlRequest: {"openvip":"1.0","id":"770e8400-e29b-41d4-a716-446655440000","command":"stt.stop"},
  } satisfies SendControlRequest;

  try {
    const data = await api.sendControl(body);
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
| **controlRequest** | [ControlRequest](ControlRequest.md) |  | |

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
| **200** | Command executed |  -  |
| **400** | Invalid command |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

