# \ControlAPI

All URIs are relative to *http://localhost:8770*

Method | HTTP request | Description
------------- | ------------- | -------------
[**SendControl**](ControlAPI.md#SendControl) | **Post** /control | Send control command



## SendControl

> Ack SendControl(ctx).ControlRequest(controlRequest).Execute()

Send control command



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	controlRequest := *openapiclient.NewControlRequest("Command_example") // ControlRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ControlAPI.SendControl(context.Background()).ControlRequest(controlRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ControlAPI.SendControl``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `SendControl`: Ack
	fmt.Fprintf(os.Stdout, "Response from `ControlAPI.SendControl`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiSendControlRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **controlRequest** | [**ControlRequest**](ControlRequest.md) |  | 

### Return type

[**Ack**](Ack.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

