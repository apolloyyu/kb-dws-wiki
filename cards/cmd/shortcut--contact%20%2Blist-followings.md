# dws contact +list-followings

kind: shortcut
completeness: full
usage: dws contact +list-followings
description: 获取当前用户的特别关注列表
source: internal/shortcut/contact/contact.go:31
visible_flags: 1

## Flags
- --open-id <String>: 可选；仅保留 openDingTalkId 精确匹配的特别关注，用于确定性存在性检查；显式传入时不能为空白

## Related
- dws contact +friend-list
- dws contact +friend-remove
- dws contact +friend-request-accept
- dws contact +friend-request-list
- dws contact +friend-request-reject
- dws contact +friend-request-send
