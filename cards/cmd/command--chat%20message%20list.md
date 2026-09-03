# dws chat message list

kind: command
completeness: full
description: Pull the recent message history of a specific conversation, including quoted-message context for merged forwards and images.
use_when: When the agent needs to read what has recently been said in a conversation and retain the context of replies.
source: internal/helpers/chat_thread.go:305
visible_flags: 4

## Flags
- --conversation-id <String> required: 会话 openConversationId (必填)
- --time <String>: 开始时间，格式: yyyy-MM-dd HH:mm:ss（可选，默认上海时间当前时间）
- --limit <Int>: 返回数量，不传则不限制
- --direction <String>: 时间方向: newer=从给定时间往现在拉，older=从给定时间往以前拉（未传 --time 时默认 older）

## Related
- dws chat message add-emoji
- dws chat message add-favorite
- dws chat message add-text-emotion
- dws chat message combine-forward
- dws chat message create-text-emotion
- dws chat message download-media
