# dws aitable field delete

kind: command
completeness: full
description: Delete a field from a datasheet by field ID; all values in that column are removed.
use_when: When the agent is cleaning up unused or deprecated columns in a datasheet.
source: internal/helpers/aitable.go:1945
visible_flags: 2

## Flags
- --base-id <String>: 待删除 Base ID。建议先通过 base get 确认目标 (必填)
- --reason <String>: 一句话描述删除的原因

## Related
- dws aitable field create
- dws aitable field get
- dws aitable field list
- dws aitable field search-options
- dws aitable field update
