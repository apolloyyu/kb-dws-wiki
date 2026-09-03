# dws oa approval approve

kind: command
completeness: full
usage: dws oa approval approve
description: Approve a pending approval process instance (task) as the current user.
example: dws oa approval approve --instance-id <id> --task-id <taskId>
use_when: When the agent acts on a pending approval the user has delegated it to handle.
source: internal/helpers/oa.go:1024
visible_flags: 3

## Flags
- --instance-id <String>: 审批实例 ID (必填)
- --task-id <String>: 审批任务 ID (必填)
- --remark <String>: 审批意见 (可选)

## Related
- dws oa approval append-task
- dws oa approval attachment
- dws oa approval create-instance
- dws oa approval detail
- dws oa approval ding-info
- dws oa approval forecast-process
