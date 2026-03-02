# MessageXAgentSwitch

Standard extension: agent routing

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **str** | Identifier of the agent to switch to | 
**confidence** | **float** | Confidence score (0.0–1.0) | [optional] 
**source** | **str** | Generator identifier — free-form string identifying the component that produced this extension | [optional] 

## Example

```python
from openvip.models.message_x_agent_switch import MessageXAgentSwitch

# TODO update the JSON string below
json = "{}"
# create an instance of MessageXAgentSwitch from a JSON string
message_x_agent_switch_instance = MessageXAgentSwitch.from_json(json)
# print the JSON string representation of the object
print(MessageXAgentSwitch.to_json())

# convert the object into a dict
message_x_agent_switch_dict = message_x_agent_switch_instance.to_dict()
# create an instance of MessageXAgentSwitch from a dict
message_x_agent_switch_from_dict = MessageXAgentSwitch.from_dict(message_x_agent_switch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


