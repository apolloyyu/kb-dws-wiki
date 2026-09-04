# dws aitable record get

kind: command
completeness: full
usage: dws aitable record get
description: 按 ID 获取记录（record query --record-ids 的便捷别名，单次最多 100 条）
example: dws aitable record get --base-id BASE_ID --table-id TABLE_ID --record-ids rec1
source: internal/helpers/aitable.go:8109
visible_flags: 0

## Flags
- none

## Related
- dws aitable record batch-update
- dws aitable record create
- dws aitable record delete
- dws aitable record group-stats
- dws aitable record history-list
- dws aitable record list
