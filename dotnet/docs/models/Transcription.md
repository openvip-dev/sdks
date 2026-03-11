# OpenVip.Model.Transcription
Voice transcription message

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Openvip** | **string** | Protocol version | 
**Type** | **string** |  | 
**Id** | **Guid** | Unique message identifier | 
**Timestamp** | **DateTime** | ISO 8601 timestamp | 
**Text** | **string** | Message text content | 
**Origin** | **string** | Producer identifier | [optional] 
**Language** | **string** | BCP 47 language tag | [optional] 
**TraceId** | **Guid** | ID of the original message (OpenTelemetry-style) | [optional] 
**ParentId** | **Guid** | ID of the parent message (OpenTelemetry-style) | [optional] 
**XInput** | [**MessageXInput**](MessageXInput.md) |  | [optional] 
**XAgentSwitch** | [**MessageXAgentSwitch**](MessageXAgentSwitch.md) |  | [optional] 
**Confidence** | **decimal** | Transcription confidence score | [optional] 
**Partial** | **bool** | If true, this is an incomplete transcription in progress | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

