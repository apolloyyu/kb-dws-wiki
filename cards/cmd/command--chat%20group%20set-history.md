# dws chat group set-history

kind: command
completeness: full
usage: dws chat group set-history
description: 设置新成员入群可查看历史消息选项
example: dws chat group set-history --conversation-id <openConversationId> --option RECENT_100
source: internal/helpers/chat.go:8826
visible_flags: 2

## Flags
- --conversation-id <String> required: 群聊 openConversationId (必填)
- --option <String> required: 可见范围: FORBIDDEN | RECENT_100 | ALL (必填)

## Related
- dws chat group audit-join-validation
- dws chat group bots
- dws chat group create
- dws chat group dismiss
- dws chat group get-by-group-id
- dws chat group get-mute-config
