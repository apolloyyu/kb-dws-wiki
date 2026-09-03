# dws chat group update-alias

kind: command
completeness: full
description: 设置群备注
source: internal/helpers/chat.go:10137
visible_flags: 2

## Flags
- --conversation-id <String> required: 群聊 openConversationId (必填)
- --alias-title <String> required: 群备注标题 (必填)

## Related
- dws chat group audit-join-validation
- dws chat group bots
- dws chat group create
- dws chat group dismiss
- dws chat group get-by-group-id
- dws chat group get-mute-config
