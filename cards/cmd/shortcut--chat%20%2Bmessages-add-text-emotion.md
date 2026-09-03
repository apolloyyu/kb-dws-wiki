# dws chat +messages-add-text-emotion

kind: shortcut
completeness: full
usage: dws chat +messages-add-text-emotion
description: 对消息添加文字表情回应
source: internal/shortcut/chat/chat_message.go:1378
visible_flags: 6

## Flags
- --conversation-id <String>: 会话 openConversationId
- --msg-id <String>: 消息 openMsgId
- --emotion-id <String>: 表情 ID（由 create-text-emotion 获取）
- --emotion-name <String>: 表情名称
- --text <String>: 文字内容
- --background-id <String>: 背景 ID

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
