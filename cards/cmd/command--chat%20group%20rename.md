# dws chat group rename

kind: command
completeness: full
description: Update the display name of a group chat.
use_when: When the agent is rebranding or clarifying the purpose of an existing group.
source: internal/helpers/chat.go:3138
visible_flags: 2

## Flags
- --id <String> required: 群 ID / openconversation_id (必填)
- --name <String> required: 修改后的群名称 (必填)

## Related
- dws chat group audit-join-validation
- dws chat group bots
- dws chat group create
- dws chat group dismiss
- dws chat group get-by-group-id
- dws chat group get-mute-config
