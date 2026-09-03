# dws chat group upgrade-to-external

kind: command
completeness: full
usage: dws chat group upgrade-to-external
description: [危险] 将普通群升级为外部群
example: dws chat group upgrade-to-external --conversation-id <openConversationId> --dry-run
source: internal/helpers/chat.go:10747
visible_flags: 2

## Flags
- --conversation-id <String> required: 待升级普通群的 openConversationId (必填)
- --extension <String>: dws

## Related
- dws chat group audit-join-validation
- dws chat group bots
- dws chat group create
- dws chat group dismiss
- dws chat group get-by-group-id
- dws chat group get-mute-config
