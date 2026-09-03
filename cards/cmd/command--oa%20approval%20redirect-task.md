# dws oa approval redirect-task

kind: command
completeness: full
description: 转交审批任务给其他人
source: internal/helpers/oa.go:1584
visible_flags: 3

## Flags
- --task-id <String>: 审批任务 ID (必填)
- --to-actioner-id <String>: 转交目标用户 ID (必填)
- --remark <String>: 转交说明 (可选)

## Related
- dws oa approval approve
- dws oa approval create-instance
- dws oa approval detail
- dws oa approval forecast-process
- dws oa approval form-schema
- dws oa approval list-by-admin
