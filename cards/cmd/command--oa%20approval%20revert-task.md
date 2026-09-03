# dws oa approval revert-task

kind: command
completeness: full
usage: dws oa approval revert-task
description: 退回审批任务到指定节点（审批人或发起人）
example: dws oa approval revert-task --instance-id <processInstanceId> --task-id <taskId> --target-activity-id sid-startevent --action REVERT_FOR_RESUBMIT --remark "补充说明后重提"
source: internal/helpers/oa.go:1810
visible_flags: 5

## Flags
- --instance-id <String>: 审批实例 ID (必填)
- --task-id <String>: 审批任务 ID (必填)
- --target-activity-id <String>: 退回到的节点 ID（退回发起人固定传 sid-startevent）(必填)
- --action <String>: 退回方式：REVERT_FOR_APPROVAL（退回到审批人）/ REVERT_FOR_RESUBMIT（退回到发起人）(必填)
- --remark <String>: 退回说明 (可选)

## Related
- dws oa approval append-task
- dws oa approval approve
- dws oa approval attachment
- dws oa approval create-instance
- dws oa approval detail
- dws oa approval ding-info
