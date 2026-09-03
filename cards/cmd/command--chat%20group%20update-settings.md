# dws chat group update-settings

kind: command
completeness: full
usage: dws chat group update-settings
description: 更新群设置
example: dws chat group update-settings --conversation-id <openConversationId> --setting-key searchable --status 1
source: internal/helpers/chat.go:7495
visible_flags: 3

## Flags
- --conversation-id <String> required: 群聊 openConversationId (必填)
- --setting-key <String> required: 群设置项 key (必填)
- --status <Int>: 设置值: 0=关闭, 1=开启 (必填)

## Related
- dws chat group audit-join-validation
- dws chat group bots
- dws chat group create
- dws chat group dismiss
- dws chat group get-by-group-id
- dws chat group get-mute-config
