# dws oa approval ding-info

kind: command
completeness: full
usage: dws oa approval ding-info
description: 获取审批任务的被催办人 userId（需与 ding message send 串联使用）
example: dws oa approval ding-info --task-id <taskId>
source: internal/helpers/oa.go:1425
visible_flags: 1

## Flags
- --task-id <String>: 审批任务 ID (必填)

## Related
- dws oa approval append-task
- dws oa approval approve
- dws oa approval attachment
- dws oa approval create-instance
- dws oa approval detail
- dws oa approval forecast-process
