# dws chat +chat-search

kind: shortcut
completeness: full
description: 按关键词分页搜索群聊，支持有界自动翻页和完整性检查
source: internal/shortcut/chat/chat_group.go:39
visible_flags: 10

## Flags
- --query <String>: 群名称关键词
- --keyword <String>: --query 的别名
- --limit <Int>: —
- --page-size <Int>: --limit 的 Lark 对齐别名；显式页大小必须在 1-100 之间
- --size <Int>: --limit 的旧版别名
- --cursor <String>: —
- --page-token <String>: --cursor 的 Lark 对齐别名
- --page-all <Bool>: 自动读取全部群搜索分页；--page-limit 仅与 --page-all 一起使用且范围 1-500
- --page-limit <Int>: —
- --exclude-muted <Bool>: 排除已设置免打扰的群聊

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
