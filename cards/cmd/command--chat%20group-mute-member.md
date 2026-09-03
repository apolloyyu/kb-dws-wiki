# dws chat group-mute-member

kind: command
completeness: full
description: 指定群成员禁言 / 取消禁言
source: internal/helpers/chat.go:7944
visible_flags: 5

## Flags
- --conversation-id <String>: 群聊 openConversationId (必填)
- --users <String>: 群成员 userId 列表，逗号分隔（批量）
- --user <String>: 群成员 userId，支持逗号分隔
- --mute-time <Int64>: 禁言时长（毫秒），支持 300000/3600000/86400000/604800000/2592000000
- --off <Bool>: 移出禁言名单（不传则加入禁言名单）

## Related
- dws chat chmod
- dws chat clear-all-red-point
- dws chat clear-messages
- dws chat clear-red-point
- dws chat conversation-info
- dws chat emotion
