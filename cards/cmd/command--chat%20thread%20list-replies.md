# dws chat thread list-replies

kind: command
completeness: full
description: List replies under an `openConvThreadId`.
use_when: When the agent needs one page of replies for a Thread.
source: internal/helpers/chat_thread.go:397
visible_flags: 5

## Flags
- --conversation-id <String> required: 父会话 openConversationId (必填)
- --topic-id <String> required: Thread openConvThreadId (必填)
- --time <String>: 开始时间，格式: yyyy-MM-dd HH:mm:ss（可选）
- --limit <Int>: 每页返回数量
- --direction <String>: 时间方向: newer=从给定时间往现在拉，older=从给定时间往以前拉（推荐，默认 older）

## Related
- dws chat thread add-emoji
- dws chat thread add-text-emotion
- dws chat thread create-group
- dws chat thread forward
- dws chat thread list
- dws chat thread list-emotion-replies
