# dws minutes mind-graph status

kind: command
completeness: full
usage: dws minutes mind-graph status
description: Query the generation status of a mind-map job and fetch the result when ready.
example: dws minutes mind-graph status --id <taskUuid>
use_when: When the agent polls after `mind-graph create` to retrieve the finished mind map.
source: internal/helpers/minutes.go:1009
visible_flags: 1

## Flags
- --id <String>: 听记 taskUuid (必填)

## Related
- dws minutes mind-graph create
