# dws chat +chat-remove-bot

kind: shortcut
completeness: full
usage: dws chat +chat-remove-bot
description: 从群内移除机器人
source: internal/shortcut/chat/chat_group.go:1399
visible_flags: 2

## Flags
- --id <String>: 群 openConversationId
- --bot-id <String>: 机器人 openBotId

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
