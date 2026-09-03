# dws oa approval forecast-process

kind: command
completeness: full
description: Forecast the approval route for a template and its proposed form values.
use_when: Before creating an instance, especially when the route contains user-selectable approver or notifier nodes.
source: internal/helpers/oa.go:1889
visible_flags: 4

## Flags
- --process-code <String>: 审批模板 processCode（简单模式使用；与 --request 互斥）
- --dept-id <String>: 发起人部门 ID（简单模式使用；与 --request 互斥）
- --form-values <String>: 表单值 JSON（简单模式使用；与 --request 互斥）
- --request <String>: 完整请求 JSON（高级模式；与简单模式参数互斥）

## Related
- dws oa approval approve
- dws oa approval create-instance
- dws oa approval detail
- dws oa approval form-schema
- dws oa approval list-by-admin
- dws oa approval list-cc
