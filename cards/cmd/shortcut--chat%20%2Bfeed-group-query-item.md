# dws chat +feed-group-query-item

kind: shortcut
completeness: full
usage: dws chat +feed-group-query-item
description: 在会话分组结果中按会话 ID 精确查询多项
source: internal/shortcut/chat/lark_alignment.go:914
visible_flags: 4

## Flags
- --category-id <Int>: —
- --conversation-ids <StringSlice>: —
- --no-detail <Bool>: 跳过精确命中会话的详情补查
- --exclude-muted <Bool>: 读取分组时排除已免打扰会话

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
