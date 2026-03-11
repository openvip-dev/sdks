# MessageXInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Ops** | **[]string** | Ordered list of input operations to perform | 
**Trigger** | Pointer to **string** | The voice phrase that triggered this action | [optional] 
**Confidence** | Pointer to **float32** | Confidence score for the trigger (0.0–1.0) | [optional] 
**Source** | Pointer to **string** | Generator identifier — free-form string identifying the component that produced this extension | [optional] 

## Methods

### NewMessageXInput

`func NewMessageXInput(ops []string, ) *MessageXInput`

NewMessageXInput instantiates a new MessageXInput object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMessageXInputWithDefaults

`func NewMessageXInputWithDefaults() *MessageXInput`

NewMessageXInputWithDefaults instantiates a new MessageXInput object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetOps

`func (o *MessageXInput) GetOps() []string`

GetOps returns the Ops field if non-nil, zero value otherwise.

### GetOpsOk

`func (o *MessageXInput) GetOpsOk() (*[]string, bool)`

GetOpsOk returns a tuple with the Ops field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOps

`func (o *MessageXInput) SetOps(v []string)`

SetOps sets Ops field to given value.


### GetTrigger

`func (o *MessageXInput) GetTrigger() string`

GetTrigger returns the Trigger field if non-nil, zero value otherwise.

### GetTriggerOk

`func (o *MessageXInput) GetTriggerOk() (*string, bool)`

GetTriggerOk returns a tuple with the Trigger field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrigger

`func (o *MessageXInput) SetTrigger(v string)`

SetTrigger sets Trigger field to given value.

### HasTrigger

`func (o *MessageXInput) HasTrigger() bool`

HasTrigger returns a boolean if a field has been set.

### GetConfidence

`func (o *MessageXInput) GetConfidence() float32`

GetConfidence returns the Confidence field if non-nil, zero value otherwise.

### GetConfidenceOk

`func (o *MessageXInput) GetConfidenceOk() (*float32, bool)`

GetConfidenceOk returns a tuple with the Confidence field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetConfidence

`func (o *MessageXInput) SetConfidence(v float32)`

SetConfidence sets Confidence field to given value.

### HasConfidence

`func (o *MessageXInput) HasConfidence() bool`

HasConfidence returns a boolean if a field has been set.

### GetSource

`func (o *MessageXInput) GetSource() string`

GetSource returns the Source field if non-nil, zero value otherwise.

### GetSourceOk

`func (o *MessageXInput) GetSourceOk() (*string, bool)`

GetSourceOk returns a tuple with the Source field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSource

`func (o *MessageXInput) SetSource(v string)`

SetSource sets Source field to given value.

### HasSource

`func (o *MessageXInput) HasSource() bool`

HasSource returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


