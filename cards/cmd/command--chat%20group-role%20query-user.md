# dws chat group-role query-user

kind: command
completeness: full
usage: dws chat group-role query-user
description: 查询群成员的群身份
example: dws chat group-role query-user --conversation-id <openConversationId> --user <userId>
source: internal/helpers/chat.go:8518
visible_flags: 2

## Flags
- --conversation-id <String> required: 群聊 openConversationId (必填)
- --user <String>: 用户 userId（必填）

## Related
- dws chat group-role add
- dws chat group-role list
- dws chat group-role remove
- dws chat group-role remove-user
- dws chat group-role set-user
- dws chat group-role update
