# dws chat toolbar sort

kind: command
completeness: partial
usage: dws chat toolbar sort
description: 排序快捷栏入口
example: dws chat toolbar sort --conversation-id <cid> --sorted-ids 101,102,103
source: internal/helpers/chat/toolbar_sort.go:26
visible_flags: 3
partial_reason: unverified_flags

## Flags
- --conversation-id <String> required: 会话 openConversationId
- --sorted-ids <String> required: 排序后的入口 ID 列表（逗号分隔）
- --unsorted-ids <String>: 不参与排序放在末尾的入口 ID 列表（逗号分隔）

## Related
- dws chat toolbar add
- dws chat toolbar create-custom
- dws chat toolbar hide
- dws chat toolbar list
- dws chat toolbar remove-custom
- dws chat toolbar update-custom
