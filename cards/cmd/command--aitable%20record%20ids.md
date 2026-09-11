# dws aitable record ids

kind: command
completeness: full
usage: dws aitable record ids
description: 分页获取记录 ID
example: dws aitable record ids --base-id BASE_ID --table-id TABLE_ID
source: internal/helpers/aitable.go:3380
visible_flags: 4

## Flags
- --base-id <String>: Base ID（通过 base list / base search 获取）(必填)
- --table-id <String>: Table ID（通过 base get 获取）(必填)
- --limit <Int>: 单页记录 ID 数量，范围 1～100；省略时服务端默认 100
- --cursor <String>: 分页游标；首次省略，后续原样传回 nextCursor

## Related
- dws aitable record batch-update
- dws aitable record create
- dws aitable record create-sub
- dws aitable record delete
- dws aitable record get
- dws aitable record group-stats
