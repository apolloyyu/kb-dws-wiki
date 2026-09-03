# dws chat emotion send

kind: command
completeness: full
usage: dws chat emotion send
description: Send a personal favorite emotion to a group or direct chat as the authenticated user.
example: dws chat emotion send --media-id <mediaId> --group <openConversationId>
use_when: When the agent needs to send a known personal emotion mediaId to exactly one group, userId, or openDingTalkId target.
source: internal/helpers/chat_personal_emotion.go:86
visible_flags: 8

## Flags
- --media-id <String>: 表情媒体 ID (必填)
- --emotion-id <String>: 表情 ID
- --conversation-id <String>: 群聊 openConversationId
- --group <String>: 群聊 openConversationId（--conversation-id 别名）
- --user <String>: 单聊接收人 userId；CLI 会解析为 openDingTalkId
- --open-dingtalk-id <String>: 单聊接收人 openDingTalkId
- --uuid <String>: 幂等键
- --idempotency-key <String>: 幂等键（--uuid 别名）

## Related
- dws chat emotion favorite
- dws chat emotion list
