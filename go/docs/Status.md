# Status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Openvip** | **string** | Protocol version | 
**Stt** | Pointer to [**StatusStt**](StatusStt.md) |  | [optional] 
**Tts** | Pointer to [**StatusTts**](StatusTts.md) |  | [optional] 
**ConnectedAgents** | Pointer to **[]string** | List of connected agent identifiers | [optional] 
**Platform** | Pointer to **map[string]interface{}** | Implementation-specific details (opaque to protocol) | [optional] 

## Methods

### NewStatus

`func NewStatus(openvip string, ) *Status`

NewStatus instantiates a new Status object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewStatusWithDefaults

`func NewStatusWithDefaults() *Status`

NewStatusWithDefaults instantiates a new Status object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetOpenvip

`func (o *Status) GetOpenvip() string`

GetOpenvip returns the Openvip field if non-nil, zero value otherwise.

### GetOpenvipOk

`func (o *Status) GetOpenvipOk() (*string, bool)`

GetOpenvipOk returns a tuple with the Openvip field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOpenvip

`func (o *Status) SetOpenvip(v string)`

SetOpenvip sets Openvip field to given value.


### GetStt

`func (o *Status) GetStt() StatusStt`

GetStt returns the Stt field if non-nil, zero value otherwise.

### GetSttOk

`func (o *Status) GetSttOk() (*StatusStt, bool)`

GetSttOk returns a tuple with the Stt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStt

`func (o *Status) SetStt(v StatusStt)`

SetStt sets Stt field to given value.

### HasStt

`func (o *Status) HasStt() bool`

HasStt returns a boolean if a field has been set.

### GetTts

`func (o *Status) GetTts() StatusTts`

GetTts returns the Tts field if non-nil, zero value otherwise.

### GetTtsOk

`func (o *Status) GetTtsOk() (*StatusTts, bool)`

GetTtsOk returns a tuple with the Tts field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTts

`func (o *Status) SetTts(v StatusTts)`

SetTts sets Tts field to given value.

### HasTts

`func (o *Status) HasTts() bool`

HasTts returns a boolean if a field has been set.

### GetConnectedAgents

`func (o *Status) GetConnectedAgents() []string`

GetConnectedAgents returns the ConnectedAgents field if non-nil, zero value otherwise.

### GetConnectedAgentsOk

`func (o *Status) GetConnectedAgentsOk() (*[]string, bool)`

GetConnectedAgentsOk returns a tuple with the ConnectedAgents field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetConnectedAgents

`func (o *Status) SetConnectedAgents(v []string)`

SetConnectedAgents sets ConnectedAgents field to given value.

### HasConnectedAgents

`func (o *Status) HasConnectedAgents() bool`

HasConnectedAgents returns a boolean if a field has been set.

### GetPlatform

`func (o *Status) GetPlatform() map[string]interface{}`

GetPlatform returns the Platform field if non-nil, zero value otherwise.

### GetPlatformOk

`func (o *Status) GetPlatformOk() (*map[string]interface{}, bool)`

GetPlatformOk returns a tuple with the Platform field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlatform

`func (o *Status) SetPlatform(v map[string]interface{})`

SetPlatform sets Platform field to given value.

### HasPlatform

`func (o *Status) HasPlatform() bool`

HasPlatform returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


