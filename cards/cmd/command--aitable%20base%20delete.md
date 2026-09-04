# dws aitable base delete

kind: command
completeness: full
usage: dws aitable base delete
description: Permanently delete an existing AI table (Base) by ID, removing all its datasheets, views, and records.
example: dws aitable base delete --base-id BASE_ID --yes
use_when: When the agent is cleaning up a Base that is no longer needed or was created for a one-off task.
source: internal/helpers/aitable.go:1957
visible_flags: 2

## Flags
- --base-id <String>: 待删除 Base ID。建议先通过 base get 确认目标 (必填)
- --reason <String>: 一句话描述删除的原因

## Related
- dws aitable base copy
- dws aitable base create
- dws aitable base get
- dws aitable base get-primary-doc-id
- dws aitable base list
- dws aitable base search
