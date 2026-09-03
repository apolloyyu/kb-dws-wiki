# dws doc +list

kind: shortcut
completeness: full
usage: dws doc +list
description: 列出文件夹或知识库下的直接子节点
source: internal/shortcut/doc/doc.go:218
visible_flags: 7

## Flags
- --folder <String>: 文档文件夹 nodeId 或 alidocs 文件夹 URL
- --workspace <String>: 知识库 ID
- --limit <Int>: 每页数量 (默认 50，最大 50)
- --cursor <String>: 分页游标 (上次结果的 nextPageToken)
- --page-all <Bool>: 有界读取全部后续页；--max-pages/--max-items 仅在 --page-all 时生效且必须大于 0
- --max-pages <Int>: —
- --max-items <Int>: —

## Related
- dws doc +background-delete
- dws doc +background-update
- dws doc +checkpoint-update
- dws doc +comment-create
- dws doc +comment-create-inline
- dws doc +comment-delete
