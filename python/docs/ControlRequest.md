# ControlRequest

Control command request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**openvip** | **str** | Protocol version | 
**id** | **UUID** | Unique request identifier (UUID v4) | 
**command** | **str** | Command to execute | 

## Example

```python
from openvip.models.control_request import ControlRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ControlRequest from a JSON string
control_request_instance = ControlRequest.from_json(json)
# print the JSON string representation of the object
print(ControlRequest.to_json())

# convert the object into a dict
control_request_dict = control_request_instance.to_dict()
# create an instance of ControlRequest from a dict
control_request_from_dict = ControlRequest.from_dict(control_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


