# MessageXInput

Standard extension: text input behavior. ops is an ordered list of input operations to perform.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ops** | **List[str]** | Ordered list of input operations to perform | 
**trigger** | **str** | The voice phrase that triggered this action | [optional] 
**confidence** | **float** | Confidence score for the trigger (0.0–1.0) | [optional] 
**source** | **str** | Generator identifier — free-form string identifying the component that produced this extension | [optional] 

## Example

```python
from openvip.models.message_x_input import MessageXInput

# TODO update the JSON string below
json = "{}"
# create an instance of MessageXInput from a JSON string
message_x_input_instance = MessageXInput.from_json(json)
# print the JSON string representation of the object
print(MessageXInput.to_json())

# convert the object into a dict
message_x_input_dict = message_x_input_instance.to_dict()
# create an instance of MessageXInput from a dict
message_x_input_from_dict = MessageXInput.from_dict(message_x_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


