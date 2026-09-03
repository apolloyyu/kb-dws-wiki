# dws chat +flag-cancel

kind: shortcut
completeness: full
usage: dws chat +flag-cancel
description: 取消收藏一条或多条消息（最多 10 条）
source: internal/shortcut/chat/lark_alignment.go:458
visible_flags: 3

## Flags
- --message-id <String>: 单条消息 openMessageId；消息 ID 去重后必须为 1-10 条
- --message-ids <StringSlice>: 多条消息 openMessageId；消息 ID 去重后必须为 1-10 条
- --conversation-id <String>: 消息所在会话 openConversationId

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
