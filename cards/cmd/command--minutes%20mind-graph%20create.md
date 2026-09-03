# dws minutes mind-graph create

kind: command
completeness: full
description: Generate a mind map from a meeting note asynchronously.
use_when: When the agent wants a structured mind-map visualization of a meeting's content.
source: internal/helpers/minutes.go:953
visible_flags: 1

## Flags
- --id <String>: 听记 taskUuid (必填)

## Related
- dws minutes mind-graph status
