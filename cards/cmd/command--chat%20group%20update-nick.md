# dws chat group update-nick

kind: command
completeness: full
usage: dws chat group update-nick
description: 设置或清除用户在群内的群昵称
example: dws chat group update-nick --conversation-id <openConversationId> --nick "我的群昵称"
source: internal/helpers/chat.go:10078
visible_flags: 2

## Flags
- --conversation-id <String> required: 群聊 openConversationId (必填)
- --nick <String>: 个人群昵称，不传则清除群昵称

## Related
- dws chat group audit-join-validation
- dws chat group bots
- dws chat group create
- dws chat group dismiss
- dws chat group get-by-group-id
- dws chat group get-mute-config
