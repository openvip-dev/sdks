# Message

Base OpenVIP message

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**openvip** | **str** | Protocol version | 
**type** | **str** | Message type | 
**id** | **UUID** | Unique message identifier | 
**timestamp** | **datetime** | ISO 8601 timestamp | 
**text** | **str** | Message text content | 
**origin** | **str** | Producer identifier | [optional] 
**language** | **str** | BCP 47 language tag | [optional] 
**trace_id** | **UUID** | ID of the original message (OpenTelemetry-style) | [optional] 
**parent_id** | **UUID** | ID of the parent message (OpenTelemetry-style) | [optional] 
**x_input** | [**MessageXInput**](MessageXInput.md) |  | [optional] 
**x_agent_switch** | [**MessageXAgentSwitch**](MessageXAgentSwitch.md) |  | [optional] 

## Example

```python
from openvip.models.message import Message

# TODO update the JSON string below
json = "{}"
# create an instance of Message from a JSON string
message_instance = Message.from_json(json)
# print the JSON string representation of the object
print(Message.to_json())

# convert the object into a dict
message_dict = message_instance.to_dict()
# create an instance of Message from a dict
message_from_dict = Message.from_dict(message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


