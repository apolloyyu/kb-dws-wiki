# dws minutes get keywords

kind: command
completeness: full
usage: dws minutes get keywords
description: Retrieve the extracted keywords of a meeting note.
example: dws minutes get keywords --id <taskUuid>
use_when: When the agent needs topical tags for a meeting without pulling the full transcript or summary.
source: internal/helpers/minutes.go:282
visible_flags: 0

## Flags
- none

## Related
- dws minutes get audio
- dws minutes get batch
- dws minutes get info
- dws minutes get summary
- dws minutes get todos
- dws minutes get transcription
