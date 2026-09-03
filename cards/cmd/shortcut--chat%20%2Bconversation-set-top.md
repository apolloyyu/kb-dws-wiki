# dws chat +conversation-set-top

kind: shortcut
completeness: full
description: 批量会话置顶 / 取消置顶（最多 10 个）
source: internal/shortcut/chat/chat_conversation.go:90
visible_flags: 3

## Flags
- --conversation-id <String>: 单个会话 openConversationId；会话 ID 去重后必须为 1-10 个
- --conversation-ids <StringSlice>: 多个会话 openConversationId；会话 ID 去重后必须为 1-10 个
- --off <Bool>: 取消置顶（不传则设置置顶）

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
