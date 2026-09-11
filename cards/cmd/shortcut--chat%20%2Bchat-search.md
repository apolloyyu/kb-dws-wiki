# dws chat +chat-search

kind: shortcut
completeness: partial
usage: dws chat +chat-search
description: 按关键词分页搜索群聊，支持有界自动翻页和完整性检查
source: internal/shortcut/chat/chat_group.go:40
visible_flags: 15
partial_reason: too_many_flags:15

## Flags
- --member-ids <StringSlice>: 候选群必须包含全部指定OpenID；最多核验100个候选，自动有界扫描
- --is-manager <Bool>: 仅本人为群主或管理员的候选群；自动有界扫描
- --chat-modes <StringSlice>: 按已验证channel筛选group/topic；未知模式报错
- --sort <String>: —
- --page-delay <Int>: —
- --query <String>: 群名称关键词
- --keyword <String>: --query 的别名
- --limit <Int>: —
- … 7 more; use dwsdoc cmd/short for full flags

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
