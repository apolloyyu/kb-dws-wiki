# dws chat group-role remove

kind: command
completeness: full
usage: dws chat group-role remove
description: 删除群身份
example: dws chat group-role remove --conversation-id <openConversationId> --role-id <openRoleId>
source: internal/helpers/chat.go:8327
visible_flags: 2

## Flags
- --conversation-id <String> required: 群聊 openConversationId (必填)
- --role-id <String> required: 群身份 openRoleId，由 group-role list 返回 (必填)

## Related
- dws chat group-role add
- dws chat group-role list
- dws chat group-role query-user
- dws chat group-role remove-user
- dws chat group-role set-user
- dws chat group-role update
