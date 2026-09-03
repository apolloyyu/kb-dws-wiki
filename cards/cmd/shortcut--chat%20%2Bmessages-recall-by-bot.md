# dws chat +messages-recall-by-bot

kind: shortcut
completeness: full
usage: dws chat +messages-recall-by-bot
description: 机器人撤回群消息
source: internal/shortcut/chat/chat_message.go:245
visible_flags: 3

## Flags
- --robot-code <String>: 机器人 Code
- --group <String>: 群 openConversationId
- --keys <StringSlice>: 发送时返回的 processQueryKey 列表

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
