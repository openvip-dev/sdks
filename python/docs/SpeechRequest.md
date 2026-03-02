# SpeechRequest

Text-to-speech request

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
**voice** | **str** | Voice identifier (engine-specific, e.g. \&quot;af_sky\&quot; for Kokoro) | [optional] 

## Example

```python
from openvip.models.speech_request import SpeechRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SpeechRequest from a JSON string
speech_request_instance = SpeechRequest.from_json(json)
# print the JSON string representation of the object
print(SpeechRequest.to_json())

# convert the object into a dict
speech_request_dict = speech_request_instance.to_dict()
# create an instance of SpeechRequest from a dict
speech_request_from_dict = SpeechRequest.from_dict(speech_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


