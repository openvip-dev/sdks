# Status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ProtocolVersion** | Pointer to **string** | Supported OpenVIP protocol version | [optional] 
**State** | Pointer to **string** | Current engine state | [optional] 
**ConnectedAgents** | Pointer to **[]string** | List of connected agent identifiers | [optional] 
**Platform** | Pointer to **map[string]interface{}** | Implementation-specific details (opaque to protocol) | [optional] 

## Methods

### NewStatus

`func NewStatus() *Status`

NewStatus instantiates a new Status object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewStatusWithDefaults

`func NewStatusWithDefaults() *Status`

NewStatusWithDefaults instantiates a new Status object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetProtocolVersion

`func (o *Status) GetProtocolVersion() string`

GetProtocolVersion returns the ProtocolVersion field if non-nil, zero value otherwise.

### GetProtocolVersionOk

`func (o *Status) GetProtocolVersionOk() (*string, bool)`

GetProtocolVersionOk returns a tuple with the ProtocolVersion field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProtocolVersion

`func (o *Status) SetProtocolVersion(v string)`

SetProtocolVersion sets ProtocolVersion field to given value.

### HasProtocolVersion

`func (o *Status) HasProtocolVersion() bool`

HasProtocolVersion returns a boolean if a field has been set.

### GetState

`func (o *Status) GetState() string`

GetState returns the State field if non-nil, zero value otherwise.

### GetStateOk

`func (o *Status) GetStateOk() (*string, bool)`

GetStateOk returns a tuple with the State field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetState

`func (o *Status) SetState(v string)`

SetState sets State field to given value.

### HasState

`func (o *Status) HasState() bool`

HasState returns a boolean if a field has been set.

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


