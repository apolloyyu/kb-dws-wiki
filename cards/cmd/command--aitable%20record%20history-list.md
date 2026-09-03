# dws aitable record history-list

kind: command
completeness: full
usage: dws aitable record history-list
description: 查询行记录变更历史
example: dws aitable record history-list --base-id BASE_ID --table-id TABLE_ID --record-id REC_ID
source: internal/helpers/aitable.go:3359
visible_flags: 5

## Flags
- --base-id <String>: 所属 Base ID (必填)
- --table-id <String>: 所属 Table ID (必填)
- --record-id <String>: 目标 Record ID (必填)
- --offset <Int>: 分页偏移量，默认 0
- --limit <Int>: 每页返回数量，默认 20，最大 50

## Related
- dws aitable record batch-update
- dws aitable record create
- dws aitable record delete
- dws aitable record get
- dws aitable record group-stats
- dws aitable record list
