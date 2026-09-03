# dws smart +chat-messages

kind: shortcut
completeness: partial
description: 读取指定群聊或单聊的消息记录，支持有界全量分页与原子 JSON 导出
source: internal/shortcut/smart/chat_messages.go:57
visible_flags: 27
partial_reason: too_many_flags:27

## Flags
- --group <String>: 群名称或 openConversationId，与单聊目标互斥
- --conversation-id <String>: --group 的别名
- --id <String>: --group 的别名
- --open-conversation-id <String>: --conversation-id 的兼容别名
- --chat-query <String>: 按群名唯一解析目标会话（可选，与其他会话目标参数互斥）
- --user <String>: 单聊对方的 userId，与 --group 互斥
- --user-query <String>: 按姓名解析唯一 openDingTalkId 的兼容入口
- --open-dingtalk-id <String>: 单聊对方的 openDingTalkId，与 --group/--user 互斥
- … 19 more; use dwsdoc cmd/short for full flags

## Related
- dws smart +access-change
- dws smart +access-grant
- dws smart +access-revoke
- dws smart +action-items
- dws smart +assign
- dws smart +assign-multi
