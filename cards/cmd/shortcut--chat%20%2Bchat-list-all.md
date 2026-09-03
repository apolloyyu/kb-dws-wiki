# dws chat +chat-list-all

kind: shortcut
completeness: full
description: 分页拉取我加入的所有群列表
source: internal/shortcut/chat/chat_group.go:854
visible_flags: 4

## Flags
- --limit <Int>: —
- --cursor <String>: 分页游标，翻页传 nextCursor
- --page-all <Bool>: 沿 nextCursor 自动读取全部已加入群；--page-limit 仅与 --page-all 一起使用且范围 1-500；--max-items/--page-delay 仅与 --page-all 一起使用；值必须大于等于 0
- --page-limit <Int>: —

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
