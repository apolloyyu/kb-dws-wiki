# dws chat message search-advanced

kind: command
completeness: full
description: 多维度搜索消息
source: internal/helpers/chat.go:4651
visible_flags: 14

## Flags
- --query <String>: 搜索关键词（可选）
- --user <String>: 发送者 userId，支持逗号分隔（可选）
- --users <String>: 发送者 userId 列表，逗号分隔（可选）
- --sender-ids <String>: 发送者 openDingTalkId 列表，逗号分隔（可选）
- --at-me <Bool>: 只搜索 @我 的消息（可选，默认 false）
- --at-ids <String>: @指定人的 openDingTalkId 列表，逗号分隔（可选）
- --conversation-ids <String>: 会话 openConversationId 列表，逗号分隔（可选，群聊或单聊均可，不传则搜索所有会话）
- --message-type <String>: 下层消息类型过滤值（可选，以当前 IM Schema 支持值为准）
- --only-robot <Bool>: 只搜索机器人消息（可选；显式传 false 时也会传给下层）
- --conversation-type <String>: 下层会话类型过滤值（可选，以当前 IM Schema 支持值为准）
- --start <String>: 开始时间，ISO-8601 格式（可选）
- --end <String>: 结束时间，ISO-8601 格式（可选）
- --cursor <String>: 分页游标（默认 \"0\"）
- --limit <Int>: 每页返回数量（默认 100）

## Related
- dws chat message add-emoji
- dws chat message add-favorite
- dws chat message add-text-emotion
- dws chat message combine-forward
- dws chat message create-text-emotion
- dws chat message download-media
