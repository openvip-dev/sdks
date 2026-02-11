# Transcription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Openvip** | **string** | Protocol version | 
**Type** | **string** | Message type | 
**Id** | **string** | Unique message identifier | 
**Timestamp** | **time.Time** | ISO 8601 timestamp | 
**Text** | **string** | Transcribed text | 
**Origin** | Pointer to **string** | Producer identifier | [optional] 
**Language** | Pointer to **string** | BCP 47 language tag | [optional] 
**Confidence** | Pointer to **float32** | Transcription confidence score | [optional] 
**Partial** | Pointer to **bool** | If true, this is an incomplete transcription in progress | [optional] 
**TraceId** | Pointer to **string** | ID of the original message (OpenTelemetry-style) | [optional] 
**ParentId** | Pointer to **string** | ID of the parent message (OpenTelemetry-style) | [optional] 

## Methods

### NewTranscription

`func NewTranscription(openvip string, type_ string, id string, timestamp time.Time, text string, ) *Transcription`

NewTranscription instantiates a new Transcription object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTranscriptionWithDefaults

`func NewTranscriptionWithDefaults() *Transcription`

NewTranscriptionWithDefaults instantiates a new Transcription object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetOpenvip

`func (o *Transcription) GetOpenvip() string`

GetOpenvip returns the Openvip field if non-nil, zero value otherwise.

### GetOpenvipOk

`func (o *Transcription) GetOpenvipOk() (*string, bool)`

GetOpenvipOk returns a tuple with the Openvip field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOpenvip

`func (o *Transcription) SetOpenvip(v string)`

SetOpenvip sets Openvip field to given value.


### GetType

`func (o *Transcription) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *Transcription) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *Transcription) SetType(v string)`

SetType sets Type field to given value.


### GetId

`func (o *Transcription) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *Transcription) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *Transcription) SetId(v string)`

SetId sets Id field to given value.


### GetTimestamp

`func (o *Transcription) GetTimestamp() time.Time`

GetTimestamp returns the Timestamp field if non-nil, zero value otherwise.

### GetTimestampOk

`func (o *Transcription) GetTimestampOk() (*time.Time, bool)`

GetTimestampOk returns a tuple with the Timestamp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTimestamp

`func (o *Transcription) SetTimestamp(v time.Time)`

SetTimestamp sets Timestamp field to given value.


### GetText

`func (o *Transcription) GetText() string`

GetText returns the Text field if non-nil, zero value otherwise.

### GetTextOk

`func (o *Transcription) GetTextOk() (*string, bool)`

GetTextOk returns a tuple with the Text field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetText

`func (o *Transcription) SetText(v string)`

SetText sets Text field to given value.


### GetOrigin

`func (o *Transcription) GetOrigin() string`

GetOrigin returns the Origin field if non-nil, zero value otherwise.

### GetOriginOk

`func (o *Transcription) GetOriginOk() (*string, bool)`

GetOriginOk returns a tuple with the Origin field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOrigin

`func (o *Transcription) SetOrigin(v string)`

SetOrigin sets Origin field to given value.

### HasOrigin

`func (o *Transcription) HasOrigin() bool`

HasOrigin returns a boolean if a field has been set.

### GetLanguage

`func (o *Transcription) GetLanguage() string`

GetLanguage returns the Language field if non-nil, zero value otherwise.

### GetLanguageOk

`func (o *Transcription) GetLanguageOk() (*string, bool)`

GetLanguageOk returns a tuple with the Language field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLanguage

`func (o *Transcription) SetLanguage(v string)`

SetLanguage sets Language field to given value.

### HasLanguage

`func (o *Transcription) HasLanguage() bool`

HasLanguage returns a boolean if a field has been set.

### GetConfidence

`func (o *Transcription) GetConfidence() float32`

GetConfidence returns the Confidence field if non-nil, zero value otherwise.

### GetConfidenceOk

`func (o *Transcription) GetConfidenceOk() (*float32, bool)`

GetConfidenceOk returns a tuple with the Confidence field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetConfidence

`func (o *Transcription) SetConfidence(v float32)`

SetConfidence sets Confidence field to given value.

### HasConfidence

`func (o *Transcription) HasConfidence() bool`

HasConfidence returns a boolean if a field has been set.

### GetPartial

`func (o *Transcription) GetPartial() bool`

GetPartial returns the Partial field if non-nil, zero value otherwise.

### GetPartialOk

`func (o *Transcription) GetPartialOk() (*bool, bool)`

GetPartialOk returns a tuple with the Partial field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPartial

`func (o *Transcription) SetPartial(v bool)`

SetPartial sets Partial field to given value.

### HasPartial

`func (o *Transcription) HasPartial() bool`

HasPartial returns a boolean if a field has been set.

### GetTraceId

`func (o *Transcription) GetTraceId() string`

GetTraceId returns the TraceId field if non-nil, zero value otherwise.

### GetTraceIdOk

`func (o *Transcription) GetTraceIdOk() (*string, bool)`

GetTraceIdOk returns a tuple with the TraceId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTraceId

`func (o *Transcription) SetTraceId(v string)`

SetTraceId sets TraceId field to given value.

### HasTraceId

`func (o *Transcription) HasTraceId() bool`

HasTraceId returns a boolean if a field has been set.

### GetParentId

`func (o *Transcription) GetParentId() string`

GetParentId returns the ParentId field if non-nil, zero value otherwise.

### GetParentIdOk

`func (o *Transcription) GetParentIdOk() (*string, bool)`

GetParentIdOk returns a tuple with the ParentId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParentId

`func (o *Transcription) SetParentId(v string)`

SetParentId sets ParentId field to given value.

### HasParentId

`func (o *Transcription) HasParentId() bool`

HasParentId returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


