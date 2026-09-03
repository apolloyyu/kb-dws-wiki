# dws chat group-role set-user

kind: command
completeness: full
description: 设置用户的群身份（覆盖该用户的全部群身份）
source: internal/helpers/chat.go:8377
visible_flags: 3

## Flags
- --conversation-id <String> required: 群聊 openConversationId (必填)
- --user <String>: 用户 userId（必填）
- --role-id <String> required: 群身份 openRoleId，由 group-role list 返回 (必填)

## Related
- dws chat group-role add
- dws chat group-role list
- dws chat group-role query-user
- dws chat group-role remove
- dws chat group-role remove-user
- dws chat group-role update
