# dws chat message add-text-emotion

kind: command
completeness: full
usage: dws chat message add-text-emotion
description: 对消息添加文字表情回应
example: dws chat message add-text-emotion --conversation-id <openConversationId> --message-id <openMsgId> --emotion-id <emotionId> --emotion-name "赞" --text "nice" --background-id im_bg_5
source: internal/helpers/chat.go:6386
visible_flags: 10

## Flags
- --conversation-id <String>: 会话 openConversationId (必填，支持单聊/群聊)
- --group <String>: --conversation-id 的别名
- --id <String>: --conversation-id 的别名
- --chat <String>: --conversation-id 的别名
- --open-conversation-id <String>: --conversation-id 的别名
- --message-id <String>: 消息 openMsgId (必填)
- --emotion-id <String>: 表情 ID (必填，通过 create-text-emotion 获取)
- --emotion-name <String>: 表情名称 (必填)
- --text <String>: 文字内容 (必填)
- --background-id <String>: 背景 ID (必填)

## Related
- dws chat message add-emoji
- dws chat message add-favorite
- dws chat message combine-forward
- dws chat message create-text-emotion
- dws chat message download-media
- dws chat message edit
