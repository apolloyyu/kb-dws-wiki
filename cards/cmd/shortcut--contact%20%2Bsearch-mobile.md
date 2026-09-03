# dws contact +search-mobile

kind: shortcut
completeness: full
description: 按手机号搜索通讯录用户
source: internal/shortcut/contact/contact.go:216
visible_flags: 1

## Flags
- --mobile <String>: 手机号；--mobile 必须是至少 6 位数字的手机号，可包含国家码、空格、连字符或括号

## Related
- dws contact +get-roster
- dws contact +list-dept-members
- dws contact +list-followings
- dws contact +list-role-members
- dws contact +list-roles
- dws contact +list-roster-fields
