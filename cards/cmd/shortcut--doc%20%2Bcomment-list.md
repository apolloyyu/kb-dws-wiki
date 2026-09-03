# dws doc +comment-list

kind: shortcut
completeness: full
usage: dws doc +comment-list
description: 查询文档评论列表
source: internal/shortcut/doc/doc.go:430
visible_flags: 5

## Flags
- --node <String>: 文档 ID 或 URL
- --limit <Int>: 每页数量 (默认 50，最大 50)
- --cursor <String>: 分页游标 (上一页返回的 nextToken)
- --type <String>: 评论类型: global (全文) / inline (划词)
- --resolve-status <String>: 解决状态: resolved / unresolved

## Related
- dws doc +background-delete
- dws doc +background-update
- dws doc +checkpoint-update
- dws doc +comment-create
- dws doc +comment-create-inline
- dws doc +comment-delete
