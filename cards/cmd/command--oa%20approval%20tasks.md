# dws oa approval tasks

kind: command
completeness: full
usage: dws oa approval tasks
description: List pending approval task IDs assigned to the current user, used to drive approve/reject actions.
example: dws oa approval tasks --instance-id <processInstanceId>
use_when: When the agent needs task IDs (not just instance IDs) before calling approve/reject.
source: internal/helpers/oa.go:1310
visible_flags: 1

## Flags
- --instance-id <String>: 审批实例 ID (必填)

## Related
- dws oa approval append-task
- dws oa approval approve
- dws oa approval attachment
- dws oa approval create-instance
- dws oa approval detail
- dws oa approval ding-info
