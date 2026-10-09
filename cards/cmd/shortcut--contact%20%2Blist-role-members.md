# dws contact +list-role-members

kind: shortcut
completeness: full
usage: dws contact +list-role-members
description: 查询角色下的成员列表
source: internal/shortcut/contact/contact.go:433
visible_flags: 1

## Flags
- --id <String>: 角色 ID；--id 必须为正整数

## Related
- dws contact +friend-list
- dws contact +friend-remove
- dws contact +friend-request-accept
- dws contact +friend-request-list
- dws contact +friend-request-reject
- dws contact +friend-request-send
