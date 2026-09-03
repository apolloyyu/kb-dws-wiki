# dws oa approval approve

kind: command
completeness: full
description: Approve a pending approval process instance (task) as the current user.
use_when: When the agent acts on a pending approval the user has delegated it to handle.
source: internal/helpers/oa.go:1024
visible_flags: 3

## Flags
- --instance-id <String>: 审批实例 ID (必填)
- --task-id <String>: 审批任务 ID (必填)
- --remark <String>: 审批意见 (可选)

## Related
- dws oa approval create-instance
- dws oa approval detail
- dws oa approval forecast-process
- dws oa approval form-schema
- dws oa approval list-by-admin
- dws oa approval list-cc
