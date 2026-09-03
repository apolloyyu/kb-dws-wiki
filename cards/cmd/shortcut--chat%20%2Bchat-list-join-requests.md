# dws chat +chat-list-join-requests

kind: shortcut
completeness: full
usage: dws chat +chat-list-join-requests
description: 分页拉取入群验证记录
source: internal/shortcut/chat/chat_group.go:1179
visible_flags: 2

## Flags
- --limit <Int>: —
- --cursor <String>: 分页游标，翻页传 nextCursor

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
