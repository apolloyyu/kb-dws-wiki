# dws chat message read-status

kind: command
completeness: full
usage: dws chat message read-status
description: 查询消息的已读/未读状态
example: dws chat message read-status --conversation-id <openConversationId> --message-id <openMessageId>
source: internal/helpers/chat.go:4935
visible_flags: 5

## Flags
- --conversation-id <String> required: 会话 openConversationId (必填，群聊或单聊均可)
- --message-id <String> required: 消息 openMessageId，由 chat message list 返回 (必填)
- --user <String>: 目标用户 userId，支持逗号分隔（可选，不传则查所有接收者）
- --users <String>: 目标用户 userId 列表，逗号分隔（可选，不传则查所有接收者）
- --target-open-dingtalk-ids <String>: 目标用户 openDingTalkId 列表，逗号分隔（可选，不传则查所有接收者）

## Related
- dws chat message add-emoji
- dws chat message add-favorite
- dws chat message add-text-emotion
- dws chat message combine-forward
- dws chat message create-text-emotion
- dws chat message download-media
