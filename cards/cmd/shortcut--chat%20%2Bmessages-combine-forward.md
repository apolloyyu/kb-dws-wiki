# dws chat +messages-combine-forward

kind: shortcut
completeness: full
usage: dws chat +messages-combine-forward
description: 合并转发多条消息
source: internal/shortcut/chat/chat_message.go:2185
visible_flags: 4

## Flags
- --src-conversation-id <String>: 源会话 openConversationId
- --msg-ids <StringSlice>: 源消息 openMessageId 列表
- --dest-conversation-id <String>: 目标会话 openConversationId
- --uuid <String>: 幂等键（可选）

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
