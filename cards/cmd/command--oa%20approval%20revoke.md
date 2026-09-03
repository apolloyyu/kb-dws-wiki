# dws oa approval revoke

kind: command
completeness: full
description: Revoke an approval process instance previously initiated by the current user.
use_when: When the agent withdraws an approval request the user no longer wants to pursue.
source: internal/helpers/oa.go:1137
visible_flags: 2

## Flags
- --instance-id <String>: 审批实例 ID (必填)
- --remark <String>: 撤销说明 (可选)

## Related
- dws oa approval approve
- dws oa approval create-instance
- dws oa approval detail
- dws oa approval forecast-process
- dws oa approval form-schema
- dws oa approval list-by-admin
