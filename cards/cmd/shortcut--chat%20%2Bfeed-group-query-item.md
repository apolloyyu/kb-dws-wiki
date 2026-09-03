# dws chat +feed-group-query-item

kind: shortcut
completeness: full
description: 在会话分组结果中按会话 ID 精确查询多项
source: internal/shortcut/chat/lark_alignment.go:848
visible_flags: 3

## Flags
- --category-id <Int>: 钉钉会话分组 ID
- --conversation-ids <StringSlice>: 要精确查询的 openConversationId 列表
- --exclude-muted <Bool>: 读取分组时排除已免打扰会话

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
