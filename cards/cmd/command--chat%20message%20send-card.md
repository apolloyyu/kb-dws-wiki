# dws chat message send-card

kind: command
completeness: full
description: 创建并推送流式卡片
source: internal/helpers/chat.go:6673
visible_flags: 4

## Flags
- --conversation-id <String>: 群聊 openConversationId（群聊时必填，与 --open-dingtalk-id 互斥）
- --open-dingtalk-id <String>: 单聊接收者 openDingTalkId（单聊时必填，与 --conversation-id 互斥）
- --at-open-dingtalk-ids <String>: 群聊创建卡片时 @ 的 openDingTalkId 列表，逗号分隔（仅与 --conversation-id 一起使用）
- --at-all <Bool>: 群聊创建卡片时 @ 所有人（仅与 --conversation-id 一起使用）

## Related
- dws chat message add-emoji
- dws chat message add-favorite
- dws chat message add-text-emotion
- dws chat message combine-forward
- dws chat message create-text-emotion
- dws chat message download-media
