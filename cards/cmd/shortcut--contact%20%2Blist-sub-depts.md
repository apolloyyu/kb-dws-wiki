# dws contact +list-sub-depts

kind: shortcut
completeness: full
description: 查看指定部门的子部门
source: internal/shortcut/contact/contact.go:565
visible_flags: 1

## Flags
- --dept <Int>: 部门 ID（钉钉根部门为 1）；--dept 必须大于 0

## Related
- dws contact +get-roster
- dws contact +list-dept-members
- dws contact +list-followings
- dws contact +list-role-members
- dws contact +list-roles
- dws contact +list-roster-fields
