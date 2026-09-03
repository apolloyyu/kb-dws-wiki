# dws oa approval detail

kind: command
completeness: full
description: Retrieve full details of an approval process instance, including form fields, attachments, and state.
use_when: When the agent needs to read the content of an approval ticket before deciding on it or summarizing it.
source: internal/helpers/oa.go:974
visible_flags: 1

## Flags
- --instance-id <String>: 审批实例 ID (必填)

## Related
- dws oa approval approve
- dws oa approval create-instance
- dws oa approval forecast-process
- dws oa approval form-schema
- dws oa approval list-by-admin
- dws oa approval list-cc
