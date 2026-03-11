# SpeechRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Openvip** | **string** | Protocol version | 
**Type** | **string** |  | 
**Id** | **string** | Unique message identifier | 
**Timestamp** | **time.Time** | ISO 8601 timestamp | 
**Text** | **string** | Message text content | 
**Origin** | Pointer to **string** | Producer identifier | [optional] 
**Language** | Pointer to **string** | BCP 47 language tag | [optional] 
**TraceId** | Pointer to **string** | ID of the original message (OpenTelemetry-style) | [optional] 
**ParentId** | Pointer to **string** | ID of the parent message (OpenTelemetry-style) | [optional] 
**XInput** | Pointer to [**MessageXInput**](MessageXInput.md) |  | [optional] 
**XAgentSwitch** | Pointer to [**MessageXAgentSwitch**](MessageXAgentSwitch.md) |  | [optional] 
**Voice** | Pointer to **string** | Voice identifier (engine-specific, e.g. \&quot;af_sky\&quot; for Kokoro) | [optional] 

## Methods

### NewSpeechRequest

`func NewSpeechRequest(openvip string, type_ string, id string, timestamp time.Time, text string, ) *SpeechRequest`

NewSpeechRequest instantiates a new SpeechRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSpeechRequestWithDefaults

`func NewSpeechRequestWithDefaults() *SpeechRequest`

NewSpeechRequestWithDefaults instantiates a new SpeechRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetOpenvip

`func (o *SpeechRequest) GetOpenvip() string`

GetOpenvip returns the Openvip field if non-nil, zero value otherwise.

### GetOpenvipOk

`func (o *SpeechRequest) GetOpenvipOk() (*string, bool)`

GetOpenvipOk returns a tuple with the Openvip field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOpenvip

`func (o *SpeechRequest) SetOpenvip(v string)`

SetOpenvip sets Openvip field to given value.


### GetType

`func (o *SpeechRequest) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *SpeechRequest) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *SpeechRequest) SetType(v string)`

SetType sets Type field to given value.


### GetId

`func (o *SpeechRequest) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *SpeechRequest) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *SpeechRequest) SetId(v string)`

SetId sets Id field to given value.


### GetTimestamp

`func (o *SpeechRequest) GetTimestamp() time.Time`

GetTimestamp returns the Timestamp field if non-nil, zero value otherwise.

### GetTimestampOk

`func (o *SpeechRequest) GetTimestampOk() (*time.Time, bool)`

GetTimestampOk returns a tuple with the Timestamp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTimestamp

`func (o *SpeechRequest) SetTimestamp(v time.Time)`

SetTimestamp sets Timestamp field to given value.


### GetText

`func (o *SpeechRequest) GetText() string`

GetText returns the Text field if non-nil, zero value otherwise.

### GetTextOk

`func (o *SpeechRequest) GetTextOk() (*string, bool)`

GetTextOk returns a tuple with the Text field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetText

`func (o *SpeechRequest) SetText(v string)`

SetText sets Text field to given value.


### GetOrigin

`func (o *SpeechRequest) GetOrigin() string`

GetOrigin returns the Origin field if non-nil, zero value otherwise.

### GetOriginOk

`func (o *SpeechRequest) GetOriginOk() (*string, bool)`

GetOriginOk returns a tuple with the Origin field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOrigin

`func (o *SpeechRequest) SetOrigin(v string)`

SetOrigin sets Origin field to given value.

### HasOrigin

`func (o *SpeechRequest) HasOrigin() bool`

HasOrigin returns a boolean if a field has been set.

### GetLanguage

`func (o *SpeechRequest) GetLanguage() string`

GetLanguage returns the Language field if non-nil, zero value otherwise.

### GetLanguageOk

`func (o *SpeechRequest) GetLanguageOk() (*string, bool)`

GetLanguageOk returns a tuple with the Language field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLanguage

`func (o *SpeechRequest) SetLanguage(v string)`

SetLanguage sets Language field to given value.

### HasLanguage

`func (o *SpeechRequest) HasLanguage() bool`

HasLanguage returns a boolean if a field has been set.

### GetTraceId

`func (o *SpeechRequest) GetTraceId() string`

GetTraceId returns the TraceId field if non-nil, zero value otherwise.

### GetTraceIdOk

`func (o *SpeechRequest) GetTraceIdOk() (*string, bool)`

GetTraceIdOk returns a tuple with the TraceId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTraceId

`func (o *SpeechRequest) SetTraceId(v string)`

SetTraceId sets TraceId field to given value.

### HasTraceId

`func (o *SpeechRequest) HasTraceId() bool`

HasTraceId returns a boolean if a field has been set.

### GetParentId

`func (o *SpeechRequest) GetParentId() string`

GetParentId returns the ParentId field if non-nil, zero value otherwise.

### GetParentIdOk

`func (o *SpeechRequest) GetParentIdOk() (*string, bool)`

GetParentIdOk returns a tuple with the ParentId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParentId

`func (o *SpeechRequest) SetParentId(v string)`

SetParentId sets ParentId field to given value.

### HasParentId

`func (o *SpeechRequest) HasParentId() bool`

HasParentId returns a boolean if a field has been set.

### GetXInput

`func (o *SpeechRequest) GetXInput() MessageXInput`

GetXInput returns the XInput field if non-nil, zero value otherwise.

### GetXInputOk

`func (o *SpeechRequest) GetXInputOk() (*MessageXInput, bool)`

GetXInputOk returns a tuple with the XInput field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetXInput

`func (o *SpeechRequest) SetXInput(v MessageXInput)`

SetXInput sets XInput field to given value.

### HasXInput

`func (o *SpeechRequest) HasXInput() bool`

HasXInput returns a boolean if a field has been set.

### GetXAgentSwitch

`func (o *SpeechRequest) GetXAgentSwitch() MessageXAgentSwitch`

GetXAgentSwitch returns the XAgentSwitch field if non-nil, zero value otherwise.

### GetXAgentSwitchOk

`func (o *SpeechRequest) GetXAgentSwitchOk() (*MessageXAgentSwitch, bool)`

GetXAgentSwitchOk returns a tuple with the XAgentSwitch field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetXAgentSwitch

`func (o *SpeechRequest) SetXAgentSwitch(v MessageXAgentSwitch)`

SetXAgentSwitch sets XAgentSwitch field to given value.

### HasXAgentSwitch

`func (o *SpeechRequest) HasXAgentSwitch() bool`

HasXAgentSwitch returns a boolean if a field has been set.

### GetVoice

`func (o *SpeechRequest) GetVoice() string`

GetVoice returns the Voice field if non-nil, zero value otherwise.

### GetVoiceOk

`func (o *SpeechRequest) GetVoiceOk() (*string, bool)`

GetVoiceOk returns a tuple with the Voice field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVoice

`func (o *SpeechRequest) SetVoice(v string)`

SetVoice sets Voice field to given value.

### HasVoice

`func (o *SpeechRequest) HasVoice() bool`

HasVoice returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


