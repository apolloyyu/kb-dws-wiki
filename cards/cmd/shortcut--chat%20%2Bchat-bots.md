# dws chat +chat-bots

kind: shortcut
completeness: full
usage: dws chat +chat-bots
description: 查看群内所有机器人
source: internal/shortcut/chat/chat_group.go:1299
visible_flags: 3

## Flags
- --group <String>: 群 openConversationId；兼容直接传群名并唯一解析
- --chat-query <String>: --group 的旧版自然名称入口
- --group-query <String>: --chat-query 的兼容别名

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
