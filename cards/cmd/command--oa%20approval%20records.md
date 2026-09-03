# dws oa approval records

kind: command
completeness: full
usage: dws oa approval records
description: Retrieve the operation history (who approved/commented/transferred, when) of an approval instance.
example: dws oa approval records --instance-id <processInstanceId>
use_when: When the agent explains an approval's progression or audits who handled it.
source: internal/helpers/oa.go:1190
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
