# ControlRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Openvip** | **string** | Protocol version | 
**Id** | **string** | Unique request identifier (UUID v4) | 
**Command** | **string** | Command to execute | 

## Methods

### NewControlRequest

`func NewControlRequest(openvip string, id string, command string, ) *ControlRequest`

NewControlRequest instantiates a new ControlRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewControlRequestWithDefaults

`func NewControlRequestWithDefaults() *ControlRequest`

NewControlRequestWithDefaults instantiates a new ControlRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetOpenvip

`func (o *ControlRequest) GetOpenvip() string`

GetOpenvip returns the Openvip field if non-nil, zero value otherwise.

### GetOpenvipOk

`func (o *ControlRequest) GetOpenvipOk() (*string, bool)`

GetOpenvipOk returns a tuple with the Openvip field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOpenvip

`func (o *ControlRequest) SetOpenvip(v string)`

SetOpenvip sets Openvip field to given value.


### GetId

`func (o *ControlRequest) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *ControlRequest) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *ControlRequest) SetId(v string)`

SetId sets Id field to given value.


### GetCommand

`func (o *ControlRequest) GetCommand() string`

GetCommand returns the Command field if non-nil, zero value otherwise.

### GetCommandOk

`func (o *ControlRequest) GetCommandOk() (*string, bool)`

GetCommandOk returns a tuple with the Command field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCommand

`func (o *ControlRequest) SetCommand(v string)`

SetCommand sets Command field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


