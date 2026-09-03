# dws chat group-role update

kind: command
completeness: full
usage: dws chat group-role update
description: 更新群身份名称
example: dws chat group-role update --conversation-id <openConversationId> --role-id <openRoleId> --name "新名称"
source: internal/helpers/chat.go:8274
visible_flags: 3

## Flags
- --conversation-id <String> required: 群聊 openConversationId (必填)
- --role-id <String> required: 群身份 openRoleId，由 group-role list 返回 (必填)
- --name <String> required: 群身份新名称 (必填)

## Related
- dws chat group-role add
- dws chat group-role list
- dws chat group-role query-user
- dws chat group-role remove
- dws chat group-role remove-user
- dws chat group-role set-user
