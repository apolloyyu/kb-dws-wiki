# dws chat group-role remove-user

kind: command
completeness: full
usage: dws chat group-role remove-user
description: 移除用户的指定群身份
example: dws chat group-role remove-user --conversation-id <openConversationId> --user <userId> --role-ids roleId1,roleId2
source: internal/helpers/chat.go:8453
visible_flags: 3

## Flags
- --conversation-id <String> required: 群聊 openConversationId (必填)
- --user <String>: 用户 userId（必填）
- --role-ids <String> required: 要移除的群身份 openRoleId 列表，逗号分隔 (必填)

## Related
- dws chat group-role add
- dws chat group-role list
- dws chat group-role query-user
- dws chat group-role remove
- dws chat group-role set-user
- dws chat group-role update
