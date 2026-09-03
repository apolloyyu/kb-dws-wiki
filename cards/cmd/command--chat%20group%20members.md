# dws chat group members

kind: command
completeness: full
usage: dws chat group members
description: List members of a group chat; can also be used against the current user to enumerate their groups' members.
example: dws chat group members --id <openconversation_id>
use_when: When the agent needs the roster of a group before mentioning, removing, or auditing members.
source: internal/helpers/chat.go:3066
visible_flags: 2

## Flags
- --id <String> required: 群 ID / openconversation_id (必填)
- --cursor <String>: 分页游标，首次从 0 开始

## Related
- dws chat group audit-join-validation
- dws chat group bots
- dws chat group create
- dws chat group dismiss
- dws chat group get-by-group-id
- dws chat group get-mute-config
