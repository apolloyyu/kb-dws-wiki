# dws chat +flag-list

kind: shortcut
completeness: full
description: 分页查询当前用户收藏的消息，支持有界自动翻页
source: internal/shortcut/chat/lark_alignment.go:517
visible_flags: 6

## Flags
- --page-size <Int>: —
- --size <Int>: —
- --page-token <String>: Lark 对齐的起始分页参数；起始 cursor 必须是非负整数
- --cursor <Int>: —
- --page-all <Bool>: 自动读取全部收藏分页；--page-limit 仅与 --page-all 一起使用且范围 1-500；--max-items/--page-delay 仅与 --page-all 一起使用；值必须大于等于 0
- --page-limit <Int>: —

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
