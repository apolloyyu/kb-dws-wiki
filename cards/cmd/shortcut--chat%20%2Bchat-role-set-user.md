# dws chat +chat-role-set-user

kind: shortcut
completeness: full
usage: dws chat +chat-role-set-user
description: 设置用户的群身份（覆盖该用户的全部群身份）
source: internal/shortcut/chat/chat_group.go:1918
visible_flags: 3

## Flags
- --group <String>: 群名或 openConversationId；群名必须唯一匹配
- --user <String>: 用户 userId 或 openDingTalkId
- --role-ids <StringSlice>: 要整体设置的群身份 openRoleId 列表；必须包含至少一个非空 openRoleId，且不能包含空值或仅含空白的元素

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
