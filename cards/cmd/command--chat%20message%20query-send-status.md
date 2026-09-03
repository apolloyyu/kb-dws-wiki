# dws chat message query-send-status

kind: command
completeness: full
usage: dws chat message query-send-status
description: 查询消息发送状态
example: dws chat message query-send-status --open-task-id <openTaskId>
source: internal/helpers/chat.go:4725
visible_flags: 1

## Flags
- --open-task-id <String> required: 消息发送任务 ID (必填)

## Related
- dws chat message add-emoji
- dws chat message add-favorite
- dws chat message add-text-emotion
- dws chat message combine-forward
- dws chat message create-text-emotion
- dws chat message download-media
