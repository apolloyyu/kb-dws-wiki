# dws contact +resolve-dept

kind: shortcut
completeness: full
usage: dws contact +resolve-dept
description: 按名称搜索部门并解析出唯一 deptId（只读）
source: internal/shortcut/smart/resolve_dept.go:47
visible_flags: 1

## Flags
- --name <String>: 要搜索的部门名称关键词（必填）

## Related
- dws contact +by-mobile
- dws contact +dept-members
- dws contact +friend-list
- dws contact +friend-remove
- dws contact +friend-request-accept
- dws contact +friend-request-list
