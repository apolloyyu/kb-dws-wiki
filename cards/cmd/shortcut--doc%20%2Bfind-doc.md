# dws doc +find-doc

kind: shortcut
completeness: full
usage: dws doc +find-doc
description: 按关键词搜索云文档并投影关键字段（只读）
source: internal/shortcut/smart/find_doc.go:44
visible_flags: 2

## Flags
- --query <String>: 按关键词搜索云文档（必填）
- --limit <Int>: 限制返回的文档条数（可选）

## Related
- dws doc +access-change
- dws doc +access-grant
- dws doc +access-revoke
- dws doc +background-delete
- dws doc +background-update
- dws doc +checkpoint-update
