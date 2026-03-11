# \MessagesAPI

All URIs are relative to *http://localhost:8770/openvip*

Method | HTTP request | Description
------------- | ------------- | -------------
[**SendMessage**](MessagesAPI.md#SendMessage) | **Post** /agents/{agent_id}/messages | Send message to agent
[**SubscribeAgent**](MessagesAPI.md#SubscribeAgent) | **Get** /agents/{agent_id}/messages | Subscribe to agent messages (SSE)



## SendMessage

> Response SendMessage(ctx, agentId).Message(message).Execute()

Send message to agent



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
    "time"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	agentId := "agentId_example" // string | Agent identifier
	message := *openapiclient.NewMessage("Openvip_example", "Type_example", "Id_example", time.Now(), "Text_example") // Message | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.MessagesAPI.SendMessage(context.Background(), agentId).Message(message).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MessagesAPI.SendMessage``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `SendMessage`: Response
	fmt.Fprintf(os.Stdout, "Response from `MessagesAPI.SendMessage`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**agentId** | **string** | Agent identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiSendMessageRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **message** | [**Message**](Message.md) |  | 

### Return type

[**Response**](Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## SubscribeAgent

> string SubscribeAgent(ctx, agentId).Execute()

Subscribe to agent messages (SSE)



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
	agentId := "agentId_example" // string | Agent identifier

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.MessagesAPI.SubscribeAgent(context.Background(), agentId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MessagesAPI.SubscribeAgent``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `SubscribeAgent`: string
	fmt.Fprintf(os.Stdout, "Response from `MessagesAPI.SubscribeAgent`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**agentId** | **string** | Agent identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiSubscribeAgentRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/event-stream, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

