# dws minutes mind-graph status

kind: command
completeness: full
description: Query the generation status of a mind-map job and fetch the result when ready.
use_when: When the agent polls after `mind-graph create` to retrieve the finished mind map.
source: internal/helpers/minutes.go:1009
visible_flags: 1

## Flags
- --id <String>: 听记 taskUuid (必填)

## Related
- dws minutes mind-graph create
