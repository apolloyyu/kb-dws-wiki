# dws oa +approve-by

kind: shortcut
completeness: full
usage: dws oa +approve-by
description: 按关键词把我的一条待审批单据一键通过（自动定位实例与任务 ID）
source: internal/shortcut/oa/smart.go:179
visible_flags: 2

## Flags
- --keyword <String>: 待审批单据的单号或标题关键词
- --comment <String>: 审批意见（可选）

## Related
- dws oa +done-approvals
- dws oa +list-forms
- dws oa +list-pending
- dws oa +my-initiated
- dws oa +pending
- dws oa +search-forms
