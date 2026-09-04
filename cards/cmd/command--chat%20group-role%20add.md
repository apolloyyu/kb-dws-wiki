# dws chat group-role add

kind: command
completeness: full
usage: dws chat group-role add
description: 添加群身份
example: dws chat group-role add --conversation-id <openConversationId> --name "管理员"
source: internal/helpers/chat.go:8427
visible_flags: 2

## Flags
- --conversation-id <String> required: 群聊 openConversationId (必填)
- --name <String> required: 群身份名称 (必填)

## Related
- dws chat group-role list
- dws chat group-role query-user
- dws chat group-role remove
- dws chat group-role remove-user
- dws chat group-role set-user
- dws chat group-role update
