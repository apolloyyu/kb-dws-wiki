# dws chat +messages-mget

kind: shortcut
completeness: full
usage: dws chat +messages-mget
description: 根据消息 ID 批量查询消息（最多 50 条）
source: internal/shortcut/chat/chat_message.go:1097
visible_flags: 3

## Flags
- --msg-ids <StringSlice>: 消息 openMsgId 列表，兼容 --message-ids / --message-id；--msg-ids 去重后必须包含 1-50 条消息 ID
- --no-reactions <Bool>: 跳过主动 Reaction 补查并不输出 Reaction（默认补查，每批最多 20 条）
- --no-threads <Bool>: 跳过 Thread 回复补查（默认每个 Thread 最多 10 条、总计最多 500 条；需要完整回复请用 +thread-replies）

## Related
- dws chat +at-me
- dws chat +bot-find
- dws chat +bot-search
- dws chat +broadcast
- dws chat +category-add-conversation
- dws chat +category-create
