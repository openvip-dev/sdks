# MessageXAgentSwitch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Target** | **string** | Identifier of the agent to switch to | 
**Confidence** | Pointer to **float32** | Confidence score (0.0–1.0) | [optional] 
**Source** | Pointer to **string** | Generator identifier — free-form string identifying the component that produced this extension | [optional] 

## Methods

### NewMessageXAgentSwitch

`func NewMessageXAgentSwitch(target string, ) *MessageXAgentSwitch`

NewMessageXAgentSwitch instantiates a new MessageXAgentSwitch object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMessageXAgentSwitchWithDefaults

`func NewMessageXAgentSwitchWithDefaults() *MessageXAgentSwitch`

NewMessageXAgentSwitchWithDefaults instantiates a new MessageXAgentSwitch object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTarget

`func (o *MessageXAgentSwitch) GetTarget() string`

GetTarget returns the Target field if non-nil, zero value otherwise.

### GetTargetOk

`func (o *MessageXAgentSwitch) GetTargetOk() (*string, bool)`

GetTargetOk returns a tuple with the Target field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTarget

`func (o *MessageXAgentSwitch) SetTarget(v string)`

SetTarget sets Target field to given value.


### GetConfidence

`func (o *MessageXAgentSwitch) GetConfidence() float32`

GetConfidence returns the Confidence field if non-nil, zero value otherwise.

### GetConfidenceOk

`func (o *MessageXAgentSwitch) GetConfidenceOk() (*float32, bool)`

GetConfidenceOk returns a tuple with the Confidence field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetConfidence

`func (o *MessageXAgentSwitch) SetConfidence(v float32)`

SetConfidence sets Confidence field to given value.

### HasConfidence

`func (o *MessageXAgentSwitch) HasConfidence() bool`

HasConfidence returns a boolean if a field has been set.

### GetSource

`func (o *MessageXAgentSwitch) GetSource() string`

GetSource returns the Source field if non-nil, zero value otherwise.

### GetSourceOk

`func (o *MessageXAgentSwitch) GetSourceOk() (*string, bool)`

GetSourceOk returns a tuple with the Source field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSource

`func (o *MessageXAgentSwitch) SetSource(v string)`

SetSource sets Source field to given value.

### HasSource

`func (o *MessageXAgentSwitch) HasSource() bool`

HasSource returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


