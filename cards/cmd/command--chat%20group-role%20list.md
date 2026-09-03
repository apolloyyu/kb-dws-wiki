# dws chat group-role list

kind: command
completeness: full
description: 分页列出群聊中的话题主消息
source: internal/helpers/chat_thread.go:305
visible_flags: 4

## Flags
- --conversation-id <String> required: 会话 openConversationId (必填)
- --time <String>: 开始时间，格式: yyyy-MM-dd HH:mm:ss（可选，默认上海时间当前时间）
- --limit <Int>: 返回数量，不传则不限制
- --direction <String>: 时间方向: newer=从给定时间往现在拉，older=从给定时间往以前拉（未传 --time 时默认 older）

## Related
- dws chat group-role add
- dws chat group-role query-user
- dws chat group-role remove
- dws chat group-role remove-user
- dws chat group-role set-user
- dws chat group-role update
