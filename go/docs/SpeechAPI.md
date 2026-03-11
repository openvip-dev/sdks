# \SpeechAPI

All URIs are relative to *http://localhost:8770/openvip*

Method | HTTP request | Description
------------- | ------------- | -------------
[**StopSpeech**](SpeechAPI.md#StopSpeech) | **Post** /speech/stop | Stop TTS playback
[**TextToSpeech**](SpeechAPI.md#TextToSpeech) | **Post** /speech | Text-to-speech request



## StopSpeech

> Response StopSpeech(ctx).Execute()

Stop TTS playback



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

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SpeechAPI.StopSpeech(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SpeechAPI.StopSpeech``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `StopSpeech`: Response
	fmt.Fprintf(os.Stdout, "Response from `SpeechAPI.StopSpeech`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiStopSpeechRequest struct via the builder pattern


### Return type

[**Response**](Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


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
    "time"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	speechRequest := *openapiclient.NewSpeechRequest("Openvip_example", "Type_example", "Id_example", time.Now(), "Text_example") // SpeechRequest | 

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

