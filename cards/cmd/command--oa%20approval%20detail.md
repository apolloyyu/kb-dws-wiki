# dws oa approval detail

kind: command
completeness: full
usage: dws oa approval detail
description: Retrieve full details of an approval process instance, including form fields, attachments, and state.
example: dws oa approval detail --instance-id <processInstanceId>
use_when: When the agent needs to read the content of an approval ticket before deciding on it or summarizing it.
source: internal/helpers/oa.go:974
visible_flags: 1

## Flags
- --instance-id <String>: 审批实例 ID (必填)

## Related
- dws oa approval append-task
- dws oa approval approve
- dws oa approval attachment
- dws oa approval create-instance
- dws oa approval ding-info
- dws oa approval forecast-process
