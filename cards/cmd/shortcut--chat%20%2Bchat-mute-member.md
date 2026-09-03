# dws chat +chat-mute-member

kind: shortcut
completeness: full
description: 指定群成员禁言 / 取消禁言
source: internal/shortcut/chat/chat_group.go:1521
visible_flags: 4

## Flags
- --group <String>: 群 openConversationId
- --users <StringSlice>: 成员 userId 或 openDingTalkId 列表
- --mute-time <Int>: 禁言时长（毫秒），如 300000/3600000/86400000/604800000/2592000000
- --off <Bool>: 移出禁言名单（不传则加入禁言名单）

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
