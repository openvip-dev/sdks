# OpenVip.Api.StatusApi

All URIs are relative to *http://localhost:8770*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**GetStatus**](StatusApi.md#getstatus) | **GET** /status | Get engine status |

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

