# dws chat group members list-by-ids

kind: command
completeness: full
description: 根据消息 ID 批量查询消息
source: internal/helpers/chat.go:6197
visible_flags: 1

## Flags
- --msg-ids <String> required: 消息 ID 列表，逗号分隔，最多 50 条 (必填)

## Related
- dws chat group members add
- dws chat group members add-bot
- dws chat group members remove
- dws chat group members remove-bot
