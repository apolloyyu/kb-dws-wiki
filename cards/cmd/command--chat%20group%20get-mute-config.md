# dws chat group get-mute-config

kind: command
completeness: full
description: 查询群用户禁言配置
source: internal/helpers/chat.go:7832
visible_flags: 2

## Flags
- --conversation-id <String>: 群聊 openConversationId (必填)
- --group <String>: --conversation-id 的别名

## Related
- dws chat group audit-join-validation
- dws chat group bots
- dws chat group create
- dws chat group dismiss
- dws chat group get-by-group-id
- dws chat group invite-url
