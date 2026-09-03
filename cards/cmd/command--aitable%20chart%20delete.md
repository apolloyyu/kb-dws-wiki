# dws aitable chart delete

kind: command
completeness: full
description: Delete a chart from a Base by chart ID.
use_when: When the agent needs to remove an obsolete or mistakenly-created chart.
source: internal/helpers/aitable.go:1945
visible_flags: 2

## Flags
- --base-id <String>: 待删除 Base ID。建议先通过 base get 确认目标 (必填)
- --reason <String>: 一句话描述删除的原因

## Related
- dws aitable chart create
- dws aitable chart get
- dws aitable chart update
- dws aitable chart widgets-example
