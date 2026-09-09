# dws chat +recent-conversations

kind: shortcut
completeness: full
usage: dws chat +recent-conversations
description: 列出指定时间以来有新消息的单聊和群聊
source: internal/shortcut/chat/active_conversations.go:51
visible_flags: 7

## Flags
- --start <String>: 开始时间（包含），选填；省略时从有效 --end 往前推 24 小时，两个时间参数都省略时查询最近 24 小时；支持 RFC3339、YYYY-MM-DD HH:mm:ss 或 YYYY-MM-DD；查询时间边界仅支持整秒，拒绝非零小数秒；
- --end <String>: 结束时间（不包含），格式同 --start；查询时间边界仅支持整秒，拒绝非零小数秒；不传时固定为本次查询当前时间向下取整秒，不包含当前未结束秒；有效整秒区间的 --end 必须晚于 --start；使用非首页 --cursor 时必须显式复
- --limit <Int>: —
- --cursor <String>: —
- --page-limit <Int>: —
- --page-delay <Int>: —
- --total-timeout <Int>: —

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
