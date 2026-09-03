# dws minutes get batch

kind: command
completeness: full
usage: dws minutes get batch
description: Batch-fetch detailed metadata for multiple meeting notes (AI minutes) by ID.
example: dws minutes get batch --ids uuid1,uuid2,uuid3
use_when: When the agent needs to enrich a list of minutes IDs with titles, durations, and participants in one call.
source: internal/helpers/minutes.go:502
visible_flags: 1

## Flags
- --ids <String>: 听记 taskUuid 列表，逗号分隔 (必填)

## Related
- dws minutes get audio
- dws minutes get info
- dws minutes get keywords
- dws minutes get summary
- dws minutes get todos
- dws minutes get transcription
