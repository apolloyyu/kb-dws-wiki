# dws oa approval search-forms

kind: command
completeness: full
usage: dws oa approval search-forms
description: 按关键字模糊搜索当前用户可见的审批表单
example: dws oa approval search-forms --query AI
source: internal/helpers/oa.go:1408
visible_flags: 1

## Flags
- --query <String>: 关键字（匹配 processCode 或表单名称）(必填)

## Related
- dws oa approval append-task
- dws oa approval approve
- dws oa approval attachment
- dws oa approval create-instance
- dws oa approval detail
- dws oa approval ding-info
