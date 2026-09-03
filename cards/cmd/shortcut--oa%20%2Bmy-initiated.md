# dws oa +my-initiated

kind: shortcut
completeness: full
description: 列出我发起（提交）的审批单据
source: internal/shortcut/oa/smart.go:111
visible_flags: 3

## Flags
- --query <String>: 关键字搜索（可选）
- --page <Int>: 分页页码（可选，默认 1）；--page 必须大于 0
- --limit <Int>: 每页大小（可选，默认 20）；--limit 必须在 1-100

## Related
- dws oa +approve-by
- dws oa +done-approvals
- dws oa +list-forms
- dws oa +list-pending
- dws oa +pending
- dws oa +search-forms
