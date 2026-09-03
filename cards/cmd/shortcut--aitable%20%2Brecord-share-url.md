# dws aitable +record-share-url

kind: shortcut
completeness: full
usage: dws aitable +record-share-url
description: 按 recordId 批量获取记录分享链接，单次最多 20 条
source: internal/shortcut/aitable/aitable.go:916
visible_flags: 4

## Flags
- --base-id <String>: Base ID
- --table-id <String>: Table ID
- --record-ids <StringSlice>: 记录 ID 列表，单次最多 20
- --view-id <String>: 视图 ID，生成带视图上下文的链接（可选）

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
