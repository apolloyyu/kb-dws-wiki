# dws chat thread list

kind: command
completeness: full
description: List topic root messages and their `openConvThreadId` values.
use_when: When the agent needs to browse topic discussions in a conversation.
source: internal/helpers/chat_thread.go:305
visible_flags: 4

## Flags
- --conversation-id <String> required: 会话 openConversationId (必填)
- --time <String>: 开始时间，格式: yyyy-MM-dd HH:mm:ss（可选，默认上海时间当前时间）
- --limit <Int>: 返回数量，不传则不限制
- --direction <String>: 时间方向: newer=从给定时间往现在拉，older=从给定时间往以前拉（未传 --time 时默认 older）

## Related
- dws chat thread add-emoji
- dws chat thread add-text-emotion
- dws chat thread create-group
- dws chat thread forward
- dws chat thread list-emotion-replies
- dws chat thread list-replies
