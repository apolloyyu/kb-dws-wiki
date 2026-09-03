# dws chat +conversation-list

kind: shortcut
completeness: full
description: 分页或一键全量获取当前用户的会话列表（单聊+群聊）
source: internal/shortcut/chat/chat_conversation.go:290
visible_flags: 5

## Flags
- --limit <Int>: —
- --cursor <Int>: 分页游标（首次不传或 0）
- --exclude-muted <Bool>: 排除已免打扰会话
- --page-all <Bool>: 自动读取全部分页；--page-limit 仅与 --page-all 一起使用且范围 1-500；--max-items/--page-delay 仅与 --page-all 一起使用；值必须大于等于 0
- --page-limit <Int>: —

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
