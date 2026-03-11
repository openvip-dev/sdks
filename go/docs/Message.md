# Message

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Openvip** | **string** | Protocol version | 
**Type** | **string** | Message type | 
**Id** | **string** | Unique message identifier | 
**Timestamp** | **time.Time** | ISO 8601 timestamp | 
**Text** | **string** | Message text content | 
**Origin** | Pointer to **string** | Producer identifier | [optional] 
**Language** | Pointer to **string** | BCP 47 language tag | [optional] 
**TraceId** | Pointer to **string** | ID of the original message (OpenTelemetry-style) | [optional] 
**ParentId** | Pointer to **string** | ID of the parent message (OpenTelemetry-style) | [optional] 
**XInput** | Pointer to [**MessageXInput**](MessageXInput.md) |  | [optional] 
**XAgentSwitch** | Pointer to [**MessageXAgentSwitch**](MessageXAgentSwitch.md) |  | [optional] 

## Methods

### NewMessage

`func NewMessage(openvip string, type_ string, id string, timestamp time.Time, text string, ) *Message`

NewMessage instantiates a new Message object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMessageWithDefaults

`func NewMessageWithDefaults() *Message`

NewMessageWithDefaults instantiates a new Message object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetOpenvip

`func (o *Message) GetOpenvip() string`

GetOpenvip returns the Openvip field if non-nil, zero value otherwise.

### GetOpenvipOk

`func (o *Message) GetOpenvipOk() (*string, bool)`

GetOpenvipOk returns a tuple with the Openvip field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOpenvip

`func (o *Message) SetOpenvip(v string)`

SetOpenvip sets Openvip field to given value.


### GetType

`func (o *Message) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *Message) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *Message) SetType(v string)`

SetType sets Type field to given value.


### GetId

`func (o *Message) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *Message) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *Message) SetId(v string)`

SetId sets Id field to given value.


### GetTimestamp

`func (o *Message) GetTimestamp() time.Time`

GetTimestamp returns the Timestamp field if non-nil, zero value otherwise.

### GetTimestampOk

`func (o *Message) GetTimestampOk() (*time.Time, bool)`

GetTimestampOk returns a tuple with the Timestamp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTimestamp

`func (o *Message) SetTimestamp(v time.Time)`

SetTimestamp sets Timestamp field to given value.


### GetText

`func (o *Message) GetText() string`

GetText returns the Text field if non-nil, zero value otherwise.

### GetTextOk

`func (o *Message) GetTextOk() (*string, bool)`

GetTextOk returns a tuple with the Text field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetText

`func (o *Message) SetText(v string)`

SetText sets Text field to given value.


### GetOrigin

`func (o *Message) GetOrigin() string`

GetOrigin returns the Origin field if non-nil, zero value otherwise.

### GetOriginOk

`func (o *Message) GetOriginOk() (*string, bool)`

GetOriginOk returns a tuple with the Origin field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOrigin

`func (o *Message) SetOrigin(v string)`

SetOrigin sets Origin field to given value.

### HasOrigin

`func (o *Message) HasOrigin() bool`

HasOrigin returns a boolean if a field has been set.

### GetLanguage

`func (o *Message) GetLanguage() string`

GetLanguage returns the Language field if non-nil, zero value otherwise.

### GetLanguageOk

`func (o *Message) GetLanguageOk() (*string, bool)`

GetLanguageOk returns a tuple with the Language field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLanguage

`func (o *Message) SetLanguage(v string)`

SetLanguage sets Language field to given value.

### HasLanguage

`func (o *Message) HasLanguage() bool`

HasLanguage returns a boolean if a field has been set.

### GetTraceId

`func (o *Message) GetTraceId() string`

GetTraceId returns the TraceId field if non-nil, zero value otherwise.

### GetTraceIdOk

`func (o *Message) GetTraceIdOk() (*string, bool)`

GetTraceIdOk returns a tuple with the TraceId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTraceId

`func (o *Message) SetTraceId(v string)`

SetTraceId sets TraceId field to given value.

### HasTraceId

`func (o *Message) HasTraceId() bool`

HasTraceId returns a boolean if a field has been set.

### GetParentId

`func (o *Message) GetParentId() string`

GetParentId returns the ParentId field if non-nil, zero value otherwise.

### GetParentIdOk

`func (o *Message) GetParentIdOk() (*string, bool)`

GetParentIdOk returns a tuple with the ParentId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParentId

`func (o *Message) SetParentId(v string)`

SetParentId sets ParentId field to given value.

### HasParentId

`func (o *Message) HasParentId() bool`

HasParentId returns a boolean if a field has been set.

### GetXInput

`func (o *Message) GetXInput() MessageXInput`

GetXInput returns the XInput field if non-nil, zero value otherwise.

### GetXInputOk

`func (o *Message) GetXInputOk() (*MessageXInput, bool)`

GetXInputOk returns a tuple with the XInput field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetXInput

`func (o *Message) SetXInput(v MessageXInput)`

SetXInput sets XInput field to given value.

### HasXInput

`func (o *Message) HasXInput() bool`

HasXInput returns a boolean if a field has been set.

### GetXAgentSwitch

`func (o *Message) GetXAgentSwitch() MessageXAgentSwitch`

GetXAgentSwitch returns the XAgentSwitch field if non-nil, zero value otherwise.

### GetXAgentSwitchOk

`func (o *Message) GetXAgentSwitchOk() (*MessageXAgentSwitch, bool)`

GetXAgentSwitchOk returns a tuple with the XAgentSwitch field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetXAgentSwitch

`func (o *Message) SetXAgentSwitch(v MessageXAgentSwitch)`

SetXAgentSwitch sets XAgentSwitch field to given value.

### HasXAgentSwitch

`func (o *Message) HasXAgentSwitch() bool`

HasXAgentSwitch returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


