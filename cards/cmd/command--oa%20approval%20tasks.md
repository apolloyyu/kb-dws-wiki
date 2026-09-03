# dws oa approval tasks

kind: command
completeness: full
description: List pending approval task IDs assigned to the current user, used to drive approve/reject actions.
use_when: When the agent needs task IDs (not just instance IDs) before calling approve/reject.
source: internal/helpers/oa.go:1310
visible_flags: 1

## Flags
- --instance-id <String>: 审批实例 ID (必填)

## Related
- dws oa approval approve
- dws oa approval create-instance
- dws oa approval detail
- dws oa approval forecast-process
- dws oa approval form-schema
- dws oa approval list-by-admin
