# dws oa approval form-schema

kind: command
completeness: full
usage: dws oa approval form-schema
description: Retrieve the form Schema for an approval template by processCode.
example: dws oa approval form-schema --process-code <processCode>
use_when: Before collecting or validating values for a new approval instance.
source: internal/helpers/oa.go:1849
visible_flags: 1

## Flags
- --process-code <String>: 审批模板 processCode (必填)

## Related
- dws oa approval append-task
- dws oa approval approve
- dws oa approval attachment
- dws oa approval create-instance
- dws oa approval detail
- dws oa approval ding-info
