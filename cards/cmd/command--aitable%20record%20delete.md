# dws aitable record delete

kind: command
completeness: full
usage: dws aitable record delete
description: Delete one or more records from a datasheet by record ID.
example: dws aitable record delete --base-id BASE_ID --table-id TABLE_ID --record-ids rec1,rec2 --yes
use_when: When the agent removes rows that are obsolete or were created in error.
source: internal/helpers/aitable.go:3185
visible_flags: 3

## Flags
- --base-id <String>: Base ID，可通过 base list 或 base search 获取 (必填)
- --table-id <String>: Table ID，可通过 base get 获取 (必填)
- --record-ids <String>: 待删除的记录 ID 列表，逗号分隔，最多 100 条 (必填)

## Related
- dws aitable record batch-update
- dws aitable record create
- dws aitable record get
- dws aitable record group-stats
- dws aitable record history-list
- dws aitable record list
