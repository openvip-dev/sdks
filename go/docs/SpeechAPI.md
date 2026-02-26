# \SpeechAPI

All URIs are relative to *http://localhost:8770*

Method | HTTP request | Description
------------- | ------------- | -------------
[**TextToSpeech**](SpeechAPI.md#TextToSpeech) | **Post** /speech | Text-to-speech request



## TextToSpeech

> SpeechResponse TextToSpeech(ctx).SpeechRequest(speechRequest).Execute()

Text-to-speech request



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/openvip-dev/sdks"
)

func main() {
	speechRequest := *openapiclient.NewSpeechRequest("1.0", "Type_example", "Light turned on") // SpeechRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SpeechAPI.TextToSpeech(context.Background()).SpeechRequest(speechRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SpeechAPI.TextToSpeech``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `TextToSpeech`: SpeechResponse
	fmt.Fprintf(os.Stdout, "Response from `SpeechAPI.TextToSpeech`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiTextToSpeechRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **speechRequest** | [**SpeechRequest**](SpeechRequest.md) |  | 

### Return type

[**SpeechResponse**](SpeechResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

