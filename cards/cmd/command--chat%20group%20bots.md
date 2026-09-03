# dws chat group bots

kind: command
completeness: full
usage: dws chat group bots
description: 查看群内所有机器人
example: dws chat group bots --group <openConversationId>
source: internal/helpers/chat.go:8590
visible_flags: 1

## Flags
- --group <String> required: 群聊 openConversationId 或需唯一解析的群名 (必填)

## Related
- dws chat group audit-join-validation
- dws chat group create
- dws chat group dismiss
- dws chat group get-by-group-id
- dws chat group get-mute-config
- dws chat group invite-url
