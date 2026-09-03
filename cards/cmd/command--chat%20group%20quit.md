# dws chat group quit

kind: command
completeness: full
usage: dws chat group quit
description: 退出群聊
example: dws chat group quit --conversation-id <openConversationId>
source: internal/helpers/chat.go:7389
visible_flags: 1

## Flags
- --conversation-id <String> required: 群聊 openConversationId (必填)

## Related
- dws chat group audit-join-validation
- dws chat group bots
- dws chat group create
- dws chat group dismiss
- dws chat group get-by-group-id
- dws chat group get-mute-config
