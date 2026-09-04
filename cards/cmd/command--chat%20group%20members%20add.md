# dws chat group members add

kind: command
completeness: full
usage: dws chat group members add
description: Add one or more users to an existing group chat.
example: dws chat group members add --id <openconversation_id> --users userId1,userId2
use_when: When the agent expands a group to include additional participants.
source: internal/helpers/chat.go:3372
visible_flags: 2

## Flags
- --id <String> required: 群 ID / openconversation_id (必填)
- --users <String> required: 要添加的用户 userId 或 openDingTalkId（可混传），逗号分隔 (必填)

## Related
- dws chat group members add-bot
- dws chat group members list-by-ids
- dws chat group members remove
- dws chat group members remove-bot
