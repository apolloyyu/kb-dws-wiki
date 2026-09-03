# dws oa approval form-schema

kind: command
completeness: full
description: Retrieve the form Schema for an approval template by processCode.
use_when: Before collecting or validating values for a new approval instance.
source: internal/helpers/oa.go:1849
visible_flags: 1

## Flags
- --process-code <String>: 审批模板 processCode (必填)

## Related
- dws oa approval approve
- dws oa approval create-instance
- dws oa approval detail
- dws oa approval forecast-process
- dws oa approval list-by-admin
- dws oa approval list-cc
