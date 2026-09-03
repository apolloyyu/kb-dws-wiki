# dws chat +chat-role-set-user

kind: shortcut
completeness: full
usage: dws chat +chat-role-set-user
description: 设置用户的群身份（覆盖该用户的全部群身份）
source: internal/shortcut/chat/chat_group.go:1882
visible_flags: 3

## Flags
- --group <String>: 群 openConversationId
- --user <String>: 用户 userId 或 openDingTalkId
- --role-ids <StringSlice>: 群身份 openRoleId 列表（空则清除全部）

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
