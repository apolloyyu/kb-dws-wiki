# dws minutes get summary

kind: command
completeness: full
usage: dws minutes get summary
description: Retrieve the AI-generated summary of a meeting note.
example: dws minutes get summary --id <taskUuid>
use_when: When the agent needs a concise recap of a meeting for reporting or follow-up.
source: internal/helpers/minutes.go:230
visible_flags: 0

## Flags
- none

## Related
- dws minutes get audio
- dws minutes get batch
- dws minutes get info
- dws minutes get keywords
- dws minutes get todos
- dws minutes get transcription
