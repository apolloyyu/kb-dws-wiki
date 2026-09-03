# dws contact +list-dept-members

kind: shortcut
completeness: full
description: 查看部门成员（仅本部门，不含下级）
source: internal/shortcut/contact/contact.go:688
visible_flags: 1

## Flags
- --depts <StringSlice>: 部门 ID 列表，逗号分隔；--depts 每项都必须为正整数且不能重复

## Related
- dws contact +get-roster
- dws contact +list-followings
- dws contact +list-role-members
- dws contact +list-roles
- dws contact +list-roster-fields
- dws contact +list-sub-depts
