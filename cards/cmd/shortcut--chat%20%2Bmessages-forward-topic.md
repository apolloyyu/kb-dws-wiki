# dws chat +messages-forward-topic

kind: shortcut
completeness: full
usage: dws chat +messages-forward-topic
description: 转发话题消息到目标会话
source: internal/shortcut/chat/chat_message.go:2213
visible_flags: 4

## Flags
- --src-msg-id <String>: 源消息 openMessageId
- --src-conversation-id <String>: 源会话 openConversationId
- --src-thread-id <String>: 话题 ID（convThread + 加密 convThreadId）
- --dest-conversation-id <String>: 目标会话 openConversationId

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
