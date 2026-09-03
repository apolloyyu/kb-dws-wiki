# dws oa +search-forms

kind: shortcut
completeness: full
description: 按关键字模糊搜索当前用户可见的审批表单
source: internal/shortcut/oa/oa.go:286
visible_flags: 1

## Flags
- --query <String>: 关键字（匹配 processCode 或表单名称）；去除空白后不能为空

## Related
- dws oa +approve-by
- dws oa +done-approvals
- dws oa +list-forms
- dws oa +list-pending
- dws oa +my-initiated
- dws oa +pending
