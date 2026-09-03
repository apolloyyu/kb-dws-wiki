# dws chat message send-a2ui-card

kind: command
completeness: full
description: 创建并推送 A2UI 卡片
source: internal/helpers/chat.go:6769
visible_flags: 3

## Flags
- --conversation-id <String>: 群聊 openConversationId（群聊时必填，与 --open-dingtalk-id 互斥）
- --open-dingtalk-id <String>: 单聊接收者 openDingTalkId（单聊时必填，与 --conversation-id 互斥）
- --content <String> required: A2UI 卡片消息 JSON 字符串数组 (必填)

## Related
- dws chat message add-emoji
- dws chat message add-favorite
- dws chat message add-text-emotion
- dws chat message combine-forward
- dws chat message create-text-emotion
- dws chat message download-media
