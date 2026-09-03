# dws chat +chat-list

kind: shortcut
completeness: full
description: 分页列出当前用户加入的会话（默认群聊；可选包含单聊）
source: internal/shortcut/chat/lark_alignment.go:935
visible_flags: 8

## Flags
- --types <StringSlice>: 会话类型只能包含 group 和/或 p2p；省略时默认只返回群聊
- --page-size <Int>: —
- --limit <Int>: --page-size 的别名，必须在 1-100 之间
- --page-token <String>: 分页游标；若提供则必须是非负整数
- --cursor <Int>: --page-token 的整数别名
- --page-all <Bool>: 自动读取全部会话分页；--page-limit 仅与 --page-all 一起使用且范围 1-500
- --page-limit <Int>: —
- --exclude-muted <Bool>: 排除已免打扰会话

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
