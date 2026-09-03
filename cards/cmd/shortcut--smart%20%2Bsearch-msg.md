# dws smart +search-msg

kind: shortcut
completeness: partial
description: 按稳定 ID、内容、时间等条件搜索消息，可校验会话范围、全量翻页并批量富化
source: internal/shortcut/smart/search_msg.go:45
visible_flags: 35
partial_reason: too_many_flags:35

## Flags
- --query <String>: 搜索关键词
- --keyword <String>: --query 的别名
- --text <String>: --query 的兼容别名
- --text-query <String>: --query 的兼容别名
- --group <String>: 单个群名或 openConversationId；自动唯一解析并校验
- --conversation-id <String>: --group 的别名
- --id <String>: --group 的别名
- --groups <StringSlice>: 多个群名或 openConversationId；可混合输入并逐项唯一解析
- … 27 more; use dwsdoc cmd/short for full flags

## Related
- dws smart +access-change
- dws smart +access-grant
- dws smart +access-revoke
- dws smart +action-items
- dws smart +assign
- dws smart +assign-multi
