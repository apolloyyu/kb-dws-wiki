# dws smart +record-share-links

kind: shortcut
completeness: full
description: 批量（可 >20 条）获取多维表记录分享链接：去重+分片+合并
source: internal/shortcut/smart/record_share_links.go:43
visible_flags: 4

## Flags
- --base <String>: Base ID（记录所属 base）
- --table <String>: Table ID（记录所属数据表）
- --record-ids <StringSlice>: 记录 ID 列表，可 >20（自动去重+分片，必填）
- --view-id <String>: 视图 ID：生成带视图上下文的链接（可选）

## Related
- dws smart +access-change
- dws smart +access-grant
- dws smart +access-revoke
- dws smart +action-items
- dws smart +assign
- dws smart +assign-multi
