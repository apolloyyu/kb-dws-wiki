# dws chat +messages-query-send-status

kind: shortcut
completeness: full
usage: dws chat +messages-query-send-status
description: 查询消息投递状态并衔接后续消息操作
source: internal/shortcut/chat/chat_message.go:1486
visible_flags: 1

## Flags
- --open-task-id <String>: 发送消息时返回的 openTaskId

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
