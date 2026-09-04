# dws chat group-role list

kind: command
completeness: full
usage: dws chat group-role list
description: 拉取会话的群身份列表
example: dws chat group-role list --conversation-id <openConversationId>
source: internal/helpers/chat.go:8379
visible_flags: 1

## Flags
- --conversation-id <String> required: 群聊 openConversationId (必填)

## Related
- dws chat group-role add
- dws chat group-role query-user
- dws chat group-role remove
- dws chat group-role remove-user
- dws chat group-role set-user
- dws chat group-role update
