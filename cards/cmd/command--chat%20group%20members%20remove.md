# dws chat group members remove

kind: command
completeness: full
description: Remove one or more members from a group chat.
use_when: When the agent kicks users who should no longer have access to the group.
source: internal/helpers/chat.go:3237
visible_flags: 2

## Flags
- --id <String> required: 群 ID / openconversation_id (必填)
- --users <String> required: 要移除的用户 userId 列表，逗号分隔 (必填)

## Related
- dws chat group members add
- dws chat group members add-bot
- dws chat group members list-by-ids
- dws chat group members remove-bot
