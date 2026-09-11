# dws chat +chat-role-remove-user

kind: shortcut
completeness: full
usage: dws chat +chat-role-remove-user
description: 移除用户的指定群身份
source: internal/shortcut/chat/chat_group.go:2225
visible_flags: 3

## Flags
- --group <String>: 群名或 openConversationId；群名必须唯一匹配
- --user <String>: 用户 userId 或 openDingTalkId
- --role-ids <StringSlice>: 要移除的群身份 openRoleId 列表；必须包含至少一个非空 openRoleId，且不能包含空值或仅含空白的元素

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
