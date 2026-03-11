# OpenVip.Api.ControlApi

All URIs are relative to *http://localhost:8770/openvip*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**SendControl**](ControlApi.md#sendcontrol) | **POST** /control | Send control command |

<a id="sendcontrol"></a>
# **SendControl**
> Response SendControl (ControlRequest controlRequest)

Send control command

Send a control command to the engine.  Available commands: - `stt.start` — Start speech-to-text - `stt.stop` — Stop speech-to-text - `engine.shutdown` — Graceful shutdown 


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **controlRequest** | [**ControlRequest**](ControlRequest.md) |  |  |

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
| **200** | Command executed |  -  |
| **400** | Invalid command |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

