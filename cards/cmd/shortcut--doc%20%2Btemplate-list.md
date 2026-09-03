# dws doc +template-list

kind: shortcut
completeness: full
usage: dws doc +template-list
description: 浏览可用文档模板；默认只读取一页
source: internal/shortcut/doc/doc.go:857
visible_flags: 6

## Flags
- --source <String>: 模板来源: MY / PUBLIC (默认 MY)
- --limit <Int>: 每页数量（默认 20）
- --cursor <String>: 分页游标
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
