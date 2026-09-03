# dws oa +done-approvals

kind: shortcut
completeness: full
description: 只读列出我已处理过的审批任务（审批历史）并投影为可读列表
source: internal/shortcut/oa/smart.go:79
visible_flags: 1

## Flags
- --limit <Int>: 最多列出多少条（可选）

## Related
- dws oa +approve-by
- dws oa +list-forms
- dws oa +list-pending
- dws oa +my-initiated
- dws oa +pending
- dws oa +search-forms
