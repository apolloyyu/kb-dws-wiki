# dws oa approval reject

kind: command
completeness: full
description: Reject a pending approval process instance as the current user.
use_when: When the agent declines an approval on behalf of the user, optionally with a reason.
source: internal/helpers/oa.go:1081
visible_flags: 3

## Flags
- --instance-id <String>: 审批实例 ID (必填)
- --task-id <String>: 审批任务 ID (必填)
- --remark <String>: 审批意见 (可选)

## Related
- dws oa approval approve
- dws oa approval create-instance
- dws oa approval detail
- dws oa approval forecast-process
- dws oa approval form-schema
- dws oa approval list-by-admin
