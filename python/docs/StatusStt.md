# StatusStt

Speech-to-text service status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | STT service available on this engine | [optional] 
**active** | **bool** | Microphone is currently listening | [optional] 

## Example

```python
from openvip.models.status_stt import StatusStt

# TODO update the JSON string below
json = "{}"
# create an instance of StatusStt from a JSON string
status_stt_instance = StatusStt.from_json(json)
# print the JSON string representation of the object
print(StatusStt.to_json())

# convert the object into a dict
status_stt_dict = status_stt_instance.to_dict()
# create an instance of StatusStt from a dict
status_stt_from_dict = StatusStt.from_dict(status_stt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


