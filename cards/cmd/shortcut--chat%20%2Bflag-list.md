# dws chat +flag-list

kind: shortcut
completeness: full
usage: dws chat +flag-list
description: 分页查询当前用户收藏的消息，支持有界自动翻页
source: internal/shortcut/chat/lark_alignment.go:561
visible_flags: 9

## Flags
- --no-enrich <Bool>: 跳过收藏消息正文/资源补查
- --with-threads <Bool>: 有界补查收藏消息Thread；每Thread10条，全查询最多50个Thread/500条回复；不可与no-enrich并用
- --no-reactions <Bool>: 跳过收藏消息主动Reaction补查
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
