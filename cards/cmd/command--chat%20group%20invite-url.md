# dws chat group invite-url

kind: command
completeness: full
description: 获取群邀请链接
source: internal/helpers/chat.go:7274
visible_flags: 2

## Flags
- --conversation-id <String> required: 群聊 openConversationId (必填)
- --expires-seconds <Int64>: 链接有效期（秒），0 表示永久有效，不传使用服务端默认值

## Related
- dws chat group audit-join-validation
- dws chat group bots
- dws chat group create
- dws chat group dismiss
- dws chat group get-by-group-id
- dws chat group get-mute-config
