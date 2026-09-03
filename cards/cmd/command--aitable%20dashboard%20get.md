# dws aitable dashboard get

kind: command
completeness: full
description: Retrieve a dashboard's layout, widget list, and metadata.
use_when: When the agent needs to inspect a dashboard before updating it or cloning it.
source: internal/helpers/aitable.go:1812
visible_flags: 1

## Flags
- --base-id <String>: Base 唯一标识。优先使用 base search / base list 返回值 (必填)

## Related
- dws aitable dashboard arrange
- dws aitable dashboard config-example
- dws aitable dashboard create
- dws aitable dashboard delete
- dws aitable dashboard update
