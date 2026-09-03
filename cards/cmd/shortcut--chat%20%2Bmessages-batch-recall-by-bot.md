# dws chat +messages-batch-recall-by-bot

kind: shortcut
completeness: full
usage: dws chat +messages-batch-recall-by-bot
description: 机器人撤回单聊消息
source: internal/shortcut/chat/chat_message.go:268
visible_flags: 2

## Flags
- --robot-code <String>: 机器人 Code
- --keys <StringSlice>: 发送时返回的 processQueryKey 列表

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
