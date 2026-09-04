# dws chat message list-pin-msg

kind: command
completeness: full
usage: dws chat message list-pin-msg
description: 拉取会话中钉住的消息列表
example: dws chat message list-pin-msg --open-conversation-id <openConversationId>
source: internal/helpers/chat.go:9308
visible_flags: 3

## Flags
- --open-conversation-id <String> required: 会话 openConversationId (必填，支持群聊/单聊)
- --cursor <String>: 分页游标（首次不传，翻页时传上次返回的 nextCursor）
- --size <Int>: 一次拉取的消息数量（默认 20，最大 100）

## Related
- dws chat message add-emoji
- dws chat message add-favorite
- dws chat message add-text-emotion
- dws chat message combine-forward
- dws chat message create-text-emotion
- dws chat message download-media
