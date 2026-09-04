# dws chat group dismiss

kind: command
completeness: full
usage: dws chat group dismiss
description: 解散群聊
example: dws chat group dismiss --conversation-id <openConversationId>
source: internal/helpers/chat.go:8973
visible_flags: 1

## Flags
- --conversation-id <String> required: 群聊 openConversationId (必填)

## Related
- dws chat group audit-join-validation
- dws chat group bots
- dws chat group create
- dws chat group get-by-group-id
- dws chat group get-mute-config
- dws chat group invite-url
