# dws chat +bot-search

kind: shortcut
completeness: full
usage: dws chat +bot-search
description: 搜索当前用户自己创建的机器人
source: internal/shortcut/chat/chat_bot.go:25
visible_flags: 3

## Flags
- --page <Int>: —
- --size <Int>: 每页数量
- --name <String>: robotName 模糊匹配

## Related
- dws chat +bot-find
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
- dws chat +category-list-conversations
