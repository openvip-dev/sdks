
# SpeechRequest

Text-to-speech request

## Properties

Name | Type
------------ | -------------
`openvip` | string
`type` | string
`id` | string
`timestamp` | Date
`text` | string
`origin` | string
`language` | string
`traceId` | string
`parentId` | string
`xInput` | [MessageXInput](MessageXInput.md)
`xAgentSwitch` | [MessageXAgentSwitch](MessageXAgentSwitch.md)
`voice` | string

## Example

```typescript
import type { SpeechRequest } from 'openvip'

// TODO: Update the object below with actual values
const example = {
  "openvip": null,
  "type": null,
  "id": null,
  "timestamp": null,
  "text": null,
  "origin": myapp/1.0.0,
  "language": en,
  "traceId": null,
  "parentId": null,
  "xInput": null,
  "xAgentSwitch": null,
  "voice": af_sky,
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


