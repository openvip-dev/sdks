# Transcription

Voice transcription message

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**openvip** | **str** | Protocol version | 
**type** | **str** |  | 
**id** | **UUID** | Unique message identifier | 
**timestamp** | **datetime** | ISO 8601 timestamp | 
**text** | **str** | Message text content | 
**origin** | **str** | Producer identifier | [optional] 
**language** | **str** | BCP 47 language tag | [optional] 
**trace_id** | **UUID** | ID of the original message (OpenTelemetry-style) | [optional] 
**parent_id** | **UUID** | ID of the parent message (OpenTelemetry-style) | [optional] 
**x_input** | [**MessageXInput**](MessageXInput.md) |  | [optional] 
**x_agent_switch** | [**MessageXAgentSwitch**](MessageXAgentSwitch.md) |  | [optional] 
**confidence** | **float** | Transcription confidence score | [optional] 
**partial** | **bool** | If true, this is an incomplete transcription in progress | [optional] 

## Example

```python
from openvip.models.transcription import Transcription

# TODO update the JSON string below
json = "{}"
# create an instance of Transcription from a JSON string
transcription_instance = Transcription.from_json(json)
# print the JSON string representation of the object
print(Transcription.to_json())

# convert the object into a dict
transcription_dict = transcription_instance.to_dict()
# create an instance of Transcription from a dict
transcription_from_dict = Transcription.from_dict(transcription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


