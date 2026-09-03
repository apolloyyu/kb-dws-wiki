# dws oa approval revoke

kind: command
completeness: full
usage: dws oa approval revoke
description: Revoke an approval process instance previously initiated by the current user.
example: dws oa approval revoke --instance-id <id> --yes
use_when: When the agent withdraws an approval request the user no longer wants to pursue.
source: internal/helpers/oa.go:1137
visible_flags: 2

## Flags
- --instance-id <String>: 审批实例 ID (必填)
- --remark <String>: 撤销说明 (可选)

## Related
- dws oa approval append-task
- dws oa approval approve
- dws oa approval attachment
- dws oa approval create-instance
- dws oa approval detail
- dws oa approval ding-info
