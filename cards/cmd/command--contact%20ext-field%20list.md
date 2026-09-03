# dws contact ext-field list

kind: command
completeness: partial
usage: dws contact ext-field list
description: 列出角色/部门成员/用户详情（兼容入口）
source: internal/helpers/contact.go:2794
visible_flags: 1
partial_reason: unverified_flags

## Flags
- --depts <String>: 部门 ID 列表

## Related
- dws contact ext-field create
- dws contact ext-field delete
- dws contact ext-field update
