# dws aitable section delete

kind: command
completeness: full
description: 删除 AI 表格
source: internal/helpers/aitable.go:1945
visible_flags: 2

## Flags
- --base-id <String>: 待删除 Base ID。建议先通过 base get 确认目标 (必填)
- --reason <String>: 一句话描述删除的原因

## Related
- dws aitable section create
- dws aitable section list-empty
- dws aitable section list-nodes
- dws aitable section move-node
- dws aitable section rename
- dws aitable section reorder
