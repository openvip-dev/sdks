# StatusTts

Text-to-speech service status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | TTS service available on this engine | [optional] 

## Example

```python
from openvip.models.status_tts import StatusTts

# TODO update the JSON string below
json = "{}"
# create an instance of StatusTts from a JSON string
status_tts_instance = StatusTts.from_json(json)
# print the JSON string representation of the object
print(StatusTts.to_json())

# convert the object into a dict
status_tts_dict = status_tts_instance.to_dict()
# create an instance of StatusTts from a dict
status_tts_from_dict = StatusTts.from_dict(status_tts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


