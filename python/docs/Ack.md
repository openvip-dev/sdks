# Ack

Acknowledgment response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Acknowledgment status | 
**id** | **UUID** | Message ID (when applicable) | [optional] 

## Example

```python
from openvip.models.ack import Ack

# TODO update the JSON string below
json = "{}"
# create an instance of Ack from a JSON string
ack_instance = Ack.from_json(json)
# print the JSON string representation of the object
print(Ack.to_json())

# convert the object into a dict
ack_dict = ack_instance.to_dict()
# create an instance of Ack from a dict
ack_from_dict = Ack.from_dict(ack_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


