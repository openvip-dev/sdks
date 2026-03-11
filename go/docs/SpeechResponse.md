# SpeechResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Openvip** | **string** | Protocol version | 
**Status** | **string** |  | 
**DurationMs** | Pointer to **int32** | Duration of the synthesized audio in milliseconds | [optional] 
**Id** | Pointer to **string** | Unique identifier for this response (assigned by the engine) | [optional] 
**Ref** | Pointer to **string** | ID of the speech request that triggered this response | [optional] 

## Methods

### NewSpeechResponse

`func NewSpeechResponse(openvip string, status string, ) *SpeechResponse`

NewSpeechResponse instantiates a new SpeechResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSpeechResponseWithDefaults

`func NewSpeechResponseWithDefaults() *SpeechResponse`

NewSpeechResponseWithDefaults instantiates a new SpeechResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetOpenvip

`func (o *SpeechResponse) GetOpenvip() string`

GetOpenvip returns the Openvip field if non-nil, zero value otherwise.

### GetOpenvipOk

`func (o *SpeechResponse) GetOpenvipOk() (*string, bool)`

GetOpenvipOk returns a tuple with the Openvip field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOpenvip

`func (o *SpeechResponse) SetOpenvip(v string)`

SetOpenvip sets Openvip field to given value.


### GetStatus

`func (o *SpeechResponse) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *SpeechResponse) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *SpeechResponse) SetStatus(v string)`

SetStatus sets Status field to given value.


### GetDurationMs

`func (o *SpeechResponse) GetDurationMs() int32`

GetDurationMs returns the DurationMs field if non-nil, zero value otherwise.

### GetDurationMsOk

`func (o *SpeechResponse) GetDurationMsOk() (*int32, bool)`

GetDurationMsOk returns a tuple with the DurationMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDurationMs

`func (o *SpeechResponse) SetDurationMs(v int32)`

SetDurationMs sets DurationMs field to given value.

### HasDurationMs

`func (o *SpeechResponse) HasDurationMs() bool`

HasDurationMs returns a boolean if a field has been set.

### GetId

`func (o *SpeechResponse) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *SpeechResponse) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *SpeechResponse) SetId(v string)`

SetId sets Id field to given value.

### HasId

`func (o *SpeechResponse) HasId() bool`

HasId returns a boolean if a field has been set.

### GetRef

`func (o *SpeechResponse) GetRef() string`

GetRef returns the Ref field if non-nil, zero value otherwise.

### GetRefOk

`func (o *SpeechResponse) GetRefOk() (*string, bool)`

GetRefOk returns a tuple with the Ref field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRef

`func (o *SpeechResponse) SetRef(v string)`

SetRef sets Ref field to given value.

### HasRef

`func (o *SpeechResponse) HasRef() bool`

HasRef returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


