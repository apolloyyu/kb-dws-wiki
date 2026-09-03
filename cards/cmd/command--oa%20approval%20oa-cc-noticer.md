# dws oa approval oa-cc-noticer

kind: command
completeness: full
description: 对审批实例进行抄送
source: internal/helpers/oa.go:1695
visible_flags: 4

## Flags
- --instance-id <String>: 审批实例 ID (必填)
- --users <String>: 抄送用户 ID 列表，多个用逗号分隔 (必填)
- --user-list <String>: 抄送用户 ID 列表，多个用逗号分隔 (必填)
- --operator-id <String>: 操作人 ID (可选)

## Related
- dws oa approval approve
- dws oa approval create-instance
- dws oa approval detail
- dws oa approval forecast-process
- dws oa approval form-schema
- dws oa approval list-by-admin
