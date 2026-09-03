# dws oa approval reject

kind: command
completeness: full
usage: dws oa approval reject
description: Reject a pending approval process instance as the current user.
example: dws oa approval reject --instance-id <id> --task-id <taskId> --remark "不同意"
use_when: When the agent declines an approval on behalf of the user, optionally with a reason.
source: internal/helpers/oa.go:1081
visible_flags: 3

## Flags
- --instance-id <String>: 审批实例 ID (必填)
- --task-id <String>: 审批任务 ID (必填)
- --remark <String>: 审批意见 (可选)

## Related
- dws oa approval append-task
- dws oa approval approve
- dws oa approval attachment
- dws oa approval create-instance
- dws oa approval detail
- dws oa approval ding-info
