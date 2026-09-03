# dws chat +conversation-info

kind: shortcut
completeness: full
usage: dws chat +conversation-info
description: 获取会话信息（群聊传 --group，单聊传 --open-dingtalk-id）
source: internal/shortcut/chat/chat_conversation.go:34
visible_flags: 2

## Flags
- --group <String>: 群聊 openConversationId
- --open-dingtalk-id <String>: 单聊对方 openDingTalkId

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
