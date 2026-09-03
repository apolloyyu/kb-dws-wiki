# dws oa approval search-forms

kind: command
completeness: full
description: 按关键字模糊搜索当前用户可见的审批表单
source: internal/helpers/oa.go:1408
visible_flags: 1

## Flags
- --query <String>: 关键字（匹配 processCode 或表单名称）(必填)

## Related
- dws oa approval approve
- dws oa approval create-instance
- dws oa approval detail
- dws oa approval forecast-process
- dws oa approval form-schema
- dws oa approval list-by-admin
