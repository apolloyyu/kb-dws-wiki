# dws chat message search-advanced

kind: command
completeness: partial
usage: dws chat message search-advanced
description: 多维度搜索消息
example: dws chat message search-advanced --query "周报" --start "2026-04-01T00:00:00+08:00" --end "2026-04-15T00:00:00+08:00"
source: internal/helpers/chat.go:4838
visible_flags: 14
partial_reason: unverified_flags

## Flags
- --query <String>: 搜索关键词（可选）
- --user <String>: 发送者 userId，支持逗号分隔（可选）
- --users <String>: 发送者 userId 列表，逗号分隔（可选）
- --sender-ids <String>: 发送者 openDingTalkId 列表，逗号分隔（可选）
- --at-me <Bool>: 只搜索 @我 的消息（可选，默认 false）
- --at-ids <String>: @指定人的 openDingTalkId 列表，逗号分隔（可选）
- --conversation-ids <String>: 会话 openConversationId 列表，逗号分隔（可选，群聊或单聊均可，不传则搜索所有会话）
- --message-type <String>: 下层消息类型过滤值（可选，以当前 IM Schema 支持值为准）
- … 6 more; use dwsdoc cmd/short for full flags

## Related
- dws chat message add-emoji
- dws chat message add-favorite
- dws chat message add-text-emotion
- dws chat message combine-forward
- dws chat message create-text-emotion
- dws chat message download-media
