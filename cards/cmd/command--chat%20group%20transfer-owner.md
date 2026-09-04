# dws chat group transfer-owner

kind: command
completeness: full
usage: dws chat group transfer-owner
description: 转让群主
example: dws chat group transfer-owner --conversation-id <openConversationId> --new-owner <openDingTalkId>
source: internal/helpers/chat.go:7402
visible_flags: 3

## Flags
- --conversation-id <String> required: 群聊 openConversationId (必填)
- --new-owner <String>: 新群主 openDingTalkId
- --user <String>: 新群主 userId

## Related
- dws chat group audit-join-validation
- dws chat group bots
- dws chat group create
- dws chat group dismiss
- dws chat group get-by-group-id
- dws chat group get-mute-config
