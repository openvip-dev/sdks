
# SpeechRequest

Text-to-speech request

## Properties

Name | Type
------------ | -------------
`openvip` | string
`type` | string
`text` | string
`language` | string

## Example

```typescript
import type { SpeechRequest } from 'openvip'

// TODO: Update the object below with actual values
const example = {
  "openvip": 1.0,
  "type": null,
  "text": Light turned on,
  "language": en,
} satisfies SpeechRequest

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as SpeechRequest
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


