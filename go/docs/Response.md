# Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Openvip** | **string** | Protocol version | 
**Status** | **string** | Operation status | 
**Id** | Pointer to **string** | Unique identifier for this response (assigned by the engine) | [optional] 
**Ref** | Pointer to **string** | ID of the request that triggered this response | [optional] 

## Methods

### NewResponse

`func NewResponse(openvip string, status string, ) *Response`

NewResponse instantiates a new Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewResponseWithDefaults

`func NewResponseWithDefaults() *Response`

NewResponseWithDefaults instantiates a new Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetOpenvip

`func (o *Response) GetOpenvip() string`

GetOpenvip returns the Openvip field if non-nil, zero value otherwise.

### GetOpenvipOk

`func (o *Response) GetOpenvipOk() (*string, bool)`

GetOpenvipOk returns a tuple with the Openvip field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOpenvip

`func (o *Response) SetOpenvip(v string)`

SetOpenvip sets Openvip field to given value.


### GetStatus

`func (o *Response) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *Response) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *Response) SetStatus(v string)`

SetStatus sets Status field to given value.


### GetId

`func (o *Response) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *Response) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *Response) SetId(v string)`

SetId sets Id field to given value.

### HasId

`func (o *Response) HasId() bool`

HasId returns a boolean if a field has been set.

### GetRef

`func (o *Response) GetRef() string`

GetRef returns the Ref field if non-nil, zero value otherwise.

### GetRefOk

`func (o *Response) GetRefOk() (*string, bool)`

GetRefOk returns a tuple with the Ref field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRef

`func (o *Response) SetRef(v string)`

SetRef sets Ref field to given value.

### HasRef

`func (o *Response) HasRef() bool`

HasRef returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


