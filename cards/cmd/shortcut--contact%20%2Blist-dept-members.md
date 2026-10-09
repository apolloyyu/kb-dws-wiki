# dws contact +list-dept-members

kind: shortcut
completeness: full
usage: dws contact +list-dept-members
description: 查看部门成员（仅本部门，不含下级）
source: internal/shortcut/contact/contact.go:688
visible_flags: 1

## Flags
- --depts <StringSlice>: 部门 ID 列表，逗号分隔；--depts 每项都必须为正整数且不能重复

## Related
- dws contact +friend-list
- dws contact +friend-remove
- dws contact +friend-request-accept
- dws contact +friend-request-list
- dws contact +friend-request-reject
- dws contact +friend-request-send
