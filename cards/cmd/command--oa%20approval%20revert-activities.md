# dws oa approval revert-activities

kind: command
completeness: full
usage: dws oa approval revert-activities
description: 获取审批任务可回退的节点信息（退回前必须调用，获取可回退节点列表）
example: dws oa approval revert-activities --task-id <taskId>
source: internal/helpers/oa.go:1790
visible_flags: 1

## Flags
- --task-id <String>: 审批任务 ID (必填)

## Related
- dws oa approval append-task
- dws oa approval approve
- dws oa approval attachment
- dws oa approval create-instance
- dws oa approval detail
- dws oa approval ding-info
