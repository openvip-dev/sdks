
# Status

Engine status

## Properties

Name | Type
------------ | -------------
`protocolVersion` | string
`state` | string
`connectedAgents` | Array&lt;string&gt;
`platform` | { [key: string]: any; }

## Example

```typescript
import type { Status } from 'openvip'

// TODO: Update the object below with actual values
const example = {
  "protocolVersion": 1.0,
  "state": listening,
  "connectedAgents": null,
  "platform": null,
} satisfies Status

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as Status
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


