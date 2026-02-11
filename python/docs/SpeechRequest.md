# SpeechRequest

Text-to-speech request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**openvip** | **str** | Protocol version | 
**type** | **str** | Message type | 
**text** | **str** | Text to synthesize | 
**language** | **str** | BCP 47 language tag | [optional] 

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


