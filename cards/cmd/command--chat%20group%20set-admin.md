# dws chat group set-admin

kind: command
completeness: full
usage: dws chat group set-admin
description: 设置 / 取消群管理员
example: dws chat group set-admin --conversation-id <openConversationId> --users userId1,userId2
source: internal/helpers/chat.go:8247
visible_flags: 4

## Flags
- --conversation-id <String> required: 群聊 openConversationId (必填)
- --users <String>: 成员 userId 列表，逗号分隔（批量）
- --user <String>: 成员 userId，支持逗号分隔
- --off <Bool>: 取消管理员（不传则设为管理员）

## Related
- dws chat group audit-join-validation
- dws chat group bots
- dws chat group create
- dws chat group dismiss
- dws chat group get-by-group-id
- dws chat group get-mute-config
