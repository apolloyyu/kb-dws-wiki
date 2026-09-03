# dws doc +template-search

kind: shortcut
completeness: full
usage: dws doc +template-search
description: 根据关键词搜索文档模板
source: internal/shortcut/doc/doc.go:925
visible_flags: 4

## Flags
- --query <String>: 搜索关键词
- --source <String>: 模板来源: MY / PUBLIC (默认 MY)
- --limit <Int>: 返回数量上限
- --cursor <String>: 分页游标

## Related
- dws doc +background-delete
- dws doc +background-update
- dws doc +checkpoint-update
- dws doc +comment-create
- dws doc +comment-create-inline
- dws doc +comment-delete
