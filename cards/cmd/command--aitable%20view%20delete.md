# dws aitable view delete

kind: command
completeness: full
description: Delete a view from a datasheet by view ID.
use_when: When the agent is cleaning up unused views.
source: internal/helpers/aitable.go:1945
visible_flags: 2

## Flags
- --base-id <String>: 待删除 Base ID。建议先通过 base get 确认目标 (必填)
- --reason <String>: 一句话描述删除的原因

## Related
- dws aitable view create
- dws aitable view duplicate
- dws aitable view get
- dws aitable view list
- dws aitable view lock
- dws aitable view update
