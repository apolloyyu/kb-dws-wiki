# dws smart +resolve-dept

kind: shortcut
completeness: full
usage: dws smart +resolve-dept
description: 按名称搜索部门并解析出唯一 deptId（只读）
source: internal/shortcut/smart/resolve_dept.go:47
visible_flags: 1

## Flags
- --name <String>: 要搜索的部门名称关键词（必填）

## Related
- dws smart +access-change
- dws smart +access-grant
- dws smart +access-revoke
- dws smart +action-items
- dws smart +assign
- dws smart +assign-multi
