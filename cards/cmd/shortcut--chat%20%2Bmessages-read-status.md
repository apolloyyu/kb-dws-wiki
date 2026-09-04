# dws chat +messages-read-status

kind: shortcut
completeness: full
usage: dws chat +messages-read-status
description: 查询消息的已读/未读状态
source: internal/shortcut/chat/chat_message.go:1535
visible_flags: 5

## Flags
- --conversation-id <String>: 会话 openConversationId
- --group <String>: --conversation-id 的别名
- --id <String>: --conversation-id 的别名
- --message-id <String>: 消息 openMessageId（当前用户发送的消息）
- --users <StringSlice>: 目标 userId 或 openDingTalkId 列表（不传返回全部接收者）

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
