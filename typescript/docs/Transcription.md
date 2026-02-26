
# Transcription

Voice transcription message

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
`confidence` | number
`partial` | boolean
`traceId` | string
`parentId` | string

## Example

```typescript
import type { Transcription } from 'openvip'

// TODO: Update the object below with actual values
const example = {
  "openvip": 1.0,
  "type": null,
  "id": null,
  "timestamp": null,
  "text": turn on the light,
  "origin": myapp/1.0.0,
  "language": en,
  "confidence": null,
  "partial": null,
  "traceId": null,
  "parentId": null,
} satisfies Transcription

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as Transcription
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


