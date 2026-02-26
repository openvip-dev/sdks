# SpeechResponse

Speech synthesis response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**openvip** | **str** | Protocol version | 
**status** | **str** |  | 
**duration_ms** | **int** | Duration of the synthesized audio in milliseconds | [optional] 
**id** | **UUID** | Unique identifier for this response (assigned by the engine) | [optional] 
**ref** | **UUID** | ID of the speech request that triggered this response | [optional] 

## Example

```python
from openvip.models.speech_response import SpeechResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SpeechResponse from a JSON string
speech_response_instance = SpeechResponse.from_json(json)
# print the JSON string representation of the object
print(SpeechResponse.to_json())

# convert the object into a dict
speech_response_dict = speech_response_instance.to_dict()
# create an instance of SpeechResponse from a dict
speech_response_from_dict = SpeechResponse.from_dict(speech_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


