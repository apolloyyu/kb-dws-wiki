# dws chat +chat-list-mine

kind: shortcut
completeness: full
usage: dws chat +chat-list-mine
description: 拉取我创建/管理的群
source: internal/shortcut/chat/chat_group.go:760
visible_flags: 3

## Flags
- --role <String>: 角色过滤
- --limit <Int>: 最多返回群数量，不传返回全部
- --exclude-muted <Bool>: 排除已设置免打扰的群聊

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
