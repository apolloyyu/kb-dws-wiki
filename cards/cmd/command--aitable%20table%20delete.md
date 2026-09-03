# dws aitable table delete

kind: command
completeness: full
usage: dws aitable table delete
description: Delete a datasheet from a Base by table ID, removing all its records, views, and fields.
example: dws aitable table delete --base-id BASE_ID --table-id TABLE_ID --yes
use_when: When the agent is disposing of a datasheet that is no longer needed.
source: internal/helpers/aitable.go:2257
visible_flags: 3

## Flags
- --base-id <String>: 目标 Base ID（通过 base list 获取）(必填)
- --table-id <String>: 将被删除的 Table ID（通过 base get / get_tables 获取）(必填)
- --reason <String>: 一句话描述一下删除该数据表的原因，用于审计

## Related
- dws aitable table create
- dws aitable table get
- dws aitable table list
- dws aitable table update
