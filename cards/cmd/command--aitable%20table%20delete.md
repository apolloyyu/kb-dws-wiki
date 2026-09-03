# dws aitable table delete

kind: command
completeness: full
description: Delete a datasheet from a Base by table ID, removing all its records, views, and fields.
use_when: When the agent is disposing of a datasheet that is no longer needed.
source: internal/helpers/aitable.go:1945
visible_flags: 2

## Flags
- --base-id <String>: 待删除 Base ID。建议先通过 base get 确认目标 (必填)
- --reason <String>: 一句话描述删除的原因

## Related
- dws aitable table create
- dws aitable table get
- dws aitable table list
- dws aitable table update
