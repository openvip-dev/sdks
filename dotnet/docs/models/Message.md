# OpenVip.Model.Message
Base OpenVIP message

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Openvip** | **string** | Protocol version | 
**Type** | **string** | Message type | 
**Id** | **Guid** | Unique message identifier | 
**Timestamp** | **DateTime** | ISO 8601 timestamp | 
**Text** | **string** | Message text content | 
**Origin** | **string** | Producer identifier | [optional] 
**Language** | **string** | BCP 47 language tag | [optional] 
**TraceId** | **Guid** | ID of the original message (OpenTelemetry-style) | [optional] 
**ParentId** | **Guid** | ID of the parent message (OpenTelemetry-style) | [optional] 
**XInput** | [**MessageXInput**](MessageXInput.md) |  | [optional] 
**XAgentSwitch** | [**MessageXAgentSwitch**](MessageXAgentSwitch.md) |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

