# dws smart +find-doc

kind: shortcut
completeness: full
description: 按关键词搜索云文档并投影关键字段（只读）
source: internal/shortcut/smart/find_doc.go:44
visible_flags: 2

## Flags
- --query <String>: 按关键词搜索云文档（必填）
- --limit <Int>: 限制返回的文档条数（可选）

## Related
- dws smart +access-change
- dws smart +access-grant
- dws smart +access-revoke
- dws smart +action-items
- dws smart +assign
- dws smart +assign-multi
