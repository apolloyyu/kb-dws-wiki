# dws oa approval create-instance

kind: command
completeness: full
description: Create a real approval process instance from validated form values or a complete request payload.
use_when: After the agent has inspected the form Schema, forecast the route, resolved any selectable approvers, and obtained explicit user confirmation.
source: internal/helpers/oa.go:2071
visible_flags: 9

## Flags
- --process-code <String>: 审批模板 processCode（简单模式使用；与 --request 互斥）
- --dept-id <String>: 发起人部门 ID
- --form-values <String>: 表单值 JSON（简单模式使用；与 --request 互斥）
- --request <String>: 完整请求 JSON（高级模式；与简单模式参数互斥）
- --originator-user-id <String>: 审批发起人 userId
- --approvers <String>: 审批人 userId 列表，多个用逗号分隔
- --approvers-action-type <String>: 审批类型：AND、OR 或 NONE
- --cc-list <String>: 抄送人 userId 列表，多个用逗号分隔
- --cc-position <String>: 抄送时点：START、FINISH 或 START_FINISH

## Related
- dws oa approval approve
- dws oa approval detail
- dws oa approval forecast-process
- dws oa approval form-schema
- dws oa approval list-by-admin
- dws oa approval list-cc
