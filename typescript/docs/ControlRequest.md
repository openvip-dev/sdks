
# ControlRequest

Control command request

## Properties

Name | Type
------------ | -------------
`openvip` | string
`id` | string
`command` | string

## Example

```typescript
import type { ControlRequest } from 'openvip'

// TODO: Update the object below with actual values
const example = {
  "openvip": null,
  "id": null,
  "command": null,
} satisfies ControlRequest

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ControlRequest
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


