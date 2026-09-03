# dws aitable record share-url

kind: command
completeness: full
usage: dws aitable record share-url
description: 批量获取记录分享链接
example: dws aitable record share-url --base-id BASE_ID --table-id TABLE_ID --record-ids rec1,rec2,rec3
source: internal/helpers/aitable.go:3428
visible_flags: 4

## Flags
- --base-id <String>: 所属 Base ID (必填)
- --table-id <String>: 所属 Table ID (必填)
- --record-ids <String>: 目标 Record ID 列表，逗号分隔，单次最多 20 条 (必填)
- --view-id <String>: 视图 ID（可选，用于生成带视图上下文的分享链接）

## Related
- dws aitable record batch-update
- dws aitable record create
- dws aitable record delete
- dws aitable record get
- dws aitable record group-stats
- dws aitable record history-list
