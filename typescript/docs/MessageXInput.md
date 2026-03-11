
# MessageXInput

Standard extension: text input behavior. ops is an ordered list of input operations to perform.

## Properties

Name | Type
------------ | -------------
`ops` | Array&lt;string&gt;
`trigger` | string
`confidence` | number
`source` | string

## Example

```typescript
import type { MessageXInput } from 'openvip'

// TODO: Update the object below with actual values
const example = {
  "ops": null,
  "trigger": null,
  "confidence": null,
  "source": null,
} satisfies MessageXInput

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as MessageXInput
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


