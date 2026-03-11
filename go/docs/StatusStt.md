# StatusStt

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Enabled** | Pointer to **bool** | STT service available on this engine | [optional] 
**Active** | Pointer to **bool** | Microphone is currently listening | [optional] 

## Methods

### NewStatusStt

`func NewStatusStt() *StatusStt`

NewStatusStt instantiates a new StatusStt object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewStatusSttWithDefaults

`func NewStatusSttWithDefaults() *StatusStt`

NewStatusSttWithDefaults instantiates a new StatusStt object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetEnabled

`func (o *StatusStt) GetEnabled() bool`

GetEnabled returns the Enabled field if non-nil, zero value otherwise.

### GetEnabledOk

`func (o *StatusStt) GetEnabledOk() (*bool, bool)`

GetEnabledOk returns a tuple with the Enabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnabled

`func (o *StatusStt) SetEnabled(v bool)`

SetEnabled sets Enabled field to given value.

### HasEnabled

`func (o *StatusStt) HasEnabled() bool`

HasEnabled returns a boolean if a field has been set.

### GetActive

`func (o *StatusStt) GetActive() bool`

GetActive returns the Active field if non-nil, zero value otherwise.

### GetActiveOk

`func (o *StatusStt) GetActiveOk() (*bool, bool)`

GetActiveOk returns a tuple with the Active field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActive

`func (o *StatusStt) SetActive(v bool)`

SetActive sets Active field to given value.

### HasActive

`func (o *StatusStt) HasActive() bool`

HasActive returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


