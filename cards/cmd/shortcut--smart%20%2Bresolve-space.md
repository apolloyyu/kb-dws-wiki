# dws smart +resolve-space

kind: shortcut
completeness: full
usage: dws smart +resolve-space
description: 按名称搜索知识空间并解析出唯一 spaceId（只读）
source: internal/shortcut/smart/resolve_space.go:46
visible_flags: 1

## Flags
- --name <String>: 要搜索的知识空间名称关键词（必填）

## Related
- dws smart +access-change
- dws smart +access-grant
- dws smart +access-revoke
- dws smart +action-items
- dws smart +assign
- dws smart +assign-multi
