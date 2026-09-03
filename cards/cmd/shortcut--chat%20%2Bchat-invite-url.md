# dws chat +chat-invite-url

kind: shortcut
completeness: full
usage: dws chat +chat-invite-url
description: 获取群邀请链接
source: internal/shortcut/chat/chat_group.go:457
visible_flags: 4

## Flags
- --group <String>: 群 openConversationId；兼容直接传群名并唯一解析
- --chat-query <String>: --group 的旧版自然名称入口
- --group-query <String>: --chat-query 的兼容别名
- --expires-seconds <Int>: 链接有效期（秒），0 表示永久

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
