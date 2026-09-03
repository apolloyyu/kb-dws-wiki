# dws chat +chat-update-settings

kind: shortcut
completeness: full
usage: dws chat +chat-update-settings
description: 更新群设置（settingKey + status）
source: internal/shortcut/chat/chat_group.go:557
visible_flags: 3

## Flags
- --group <String>: 群 openConversationId
- --setting-key <String>: 群设置项 key，如 searchable / onlyAdminCanAtAll
- --status <Int>: 设置值：0=关闭，1=开启

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
