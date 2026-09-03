# dws smart +chat-members-list

kind: shortcut
completeness: full
description: 列出群成员并把用户与机器人分桶（支持群名语义解析）
source: internal/shortcut/smart/group_members.go:109
visible_flags: 7

## Flags
- --group <String>: 群名称或 openConversationId
- --conversation-id <String>: 显式群 openConversationId
- --chat-query <String>: 按群名解析唯一 openConversationId
- --chat <String>: --conversation-id 的兼容别名
- --open-conversation-id <String>: --conversation-id 的兼容别名
- --member-types <StringSlice>: 成员类型；--member-types 仅接受 user/bot；不传则同时返回
- --page-limit <Int>: —

## Related
- dws smart +access-change
- dws smart +access-grant
- dws smart +access-revoke
- dws smart +action-items
- dws smart +assign
- dws smart +assign-multi
