# dws minutes get todos

kind: command
completeness: full
usage: dws minutes get todos
description: Retrieve the action items (todos) extracted from a meeting note.
example: dws minutes get todos --id <taskUuid>
use_when: When the agent needs to convert meeting action items into tasks or follow up on commitments.
source: internal/helpers/minutes.go:395
visible_flags: 0

## Flags
- none

## Related
- dws minutes get audio
- dws minutes get batch
- dws minutes get info
- dws minutes get keywords
- dws minutes get summary
- dws minutes get transcription
