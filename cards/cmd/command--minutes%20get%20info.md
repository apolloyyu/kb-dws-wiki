# dws minutes get info

kind: command
completeness: full
usage: dws minutes get info
description: Retrieve basic metadata for a single meeting note (title, owner, time, duration, participants).
example: dws minutes get info --id <taskUuid>
use_when: When the agent needs a header view of a specific meeting note.
source: internal/helpers/minutes.go:184
visible_flags: 0

## Flags
- none

## Related
- dws minutes get audio
- dws minutes get batch
- dws minutes get keywords
- dws minutes get summary
- dws minutes get todos
- dws minutes get transcription
