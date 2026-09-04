# dws chat +messages-resource-url

kind: shortcut
completeness: full
usage: dws chat +messages-resource-url
description: 获取消息资源（图片/视频/语音）下载链接
source: internal/shortcut/chat/chat_message.go:2123
visible_flags: 6

## Flags
- --type <String>: —
- --resource-id <String>: 资源 ID（消息中的 mediaId）
- --message-id <String>: 消息 openMessageId
- --msg-id <String>: --message-id 的别名
- --open-message-id <String>: --message-id 的别名
- --open-conversation-id <String>: 会话 openConversationId

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
