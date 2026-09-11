# dws chat message send-a2ui-card

kind: command
completeness: full
usage: dws chat message send-a2ui-card
description: 创建并推送 A2UI 卡片
example: dws chat message send-a2ui-card --conversation-id <openConversationId> --content '["{\"version\":\"v1.0\"}"]'
source: internal/helpers/chat.go:7334
visible_flags: 5

## Flags
- --conversation-id <String>: 群聊 openConversationId（群聊时必填，与 --open-dingtalk-id 互斥）
- --open-dingtalk-id <String>: 单聊接收者 openDingTalkId（单聊时必填，与 --conversation-id 互斥）
- --a2ui-annotations <String>: A2UI 组件注解 JSON 对象数组（可选，支持空数组 []）
- --support-forward <Bool>: 允许转发 A2UI 卡片（默认不允许）
- --content <String> required: A2UI 卡片消息 JSON 字符串数组 (必填)

## Related
- dws chat message add-emoji
- dws chat message add-favorite
- dws chat message add-text-emotion
- dws chat message combine-forward
- dws chat message create-text-emotion
- dws chat message download-media
