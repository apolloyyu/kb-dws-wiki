# dws chat +bot-find

kind: shortcut
completeness: full
usage: dws chat +bot-find
description: 搜索全部可用机器人（含他人/官方，返回 openDingTalkId 可发单聊）
source: internal/shortcut/chat/chat_bot.go:144
visible_flags: 4

## Flags
- --query <String>: 搜索关键词
- --keyword <String>: --query 的别名
- --limit <Int>: —
- --cursor <String>: 分页游标，翻页传 nextCursor

## Related
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
- dws chat +category-list-conversations
