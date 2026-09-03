# dws contact +list-followings

kind: shortcut
completeness: full
description: 获取当前用户的特别关注列表
source: internal/shortcut/contact/contact.go:31
visible_flags: 1

## Flags
- --open-id <String>: 可选；仅保留 openDingTalkId 精确匹配的特别关注，用于确定性存在性检查；显式传入时不能为空白

## Related
- dws contact +get-roster
- dws contact +list-dept-members
- dws contact +list-role-members
- dws contact +list-roles
- dws contact +list-roster-fields
- dws contact +list-sub-depts
