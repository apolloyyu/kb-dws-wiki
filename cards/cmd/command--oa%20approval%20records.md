# dws oa approval records

kind: command
completeness: full
description: Retrieve the operation history (who approved/commented/transferred, when) of an approval instance.
use_when: When the agent explains an approval's progression or audits who handled it.
source: internal/helpers/oa.go:1190
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
