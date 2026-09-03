# dws aitable record delete

kind: command
completeness: full
description: Delete one or more records from a datasheet by record ID.
use_when: When the agent removes rows that are obsolete or were created in error.
source: internal/helpers/aitable.go:1945
visible_flags: 2

## Flags
- --base-id <String>: 待删除 Base ID。建议先通过 base get 确认目标 (必填)
- --reason <String>: 一句话描述删除的原因

## Related
- dws aitable record batch-update
- dws aitable record create
- dws aitable record get
- dws aitable record group-stats
- dws aitable record history-list
- dws aitable record list
