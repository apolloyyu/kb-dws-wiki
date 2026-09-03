# dws oa approval list-pending

kind: command
completeness: partial
usage: dws oa approval list-pending
description: List approval process instances currently awaiting action from the current user.
example: dws oa approval list-pending --create-time-from 2026-08-01 --create-time-to 2026-08-31 --query 关键词
use_when: When the agent surfaces "needs your approval" items in the user's inbox.
source: internal/helpers/oa.go:927
visible_flags: 0
partial_reason: unverified_flags

## Flags
- none

## Related
- dws oa approval append-task
- dws oa approval approve
- dws oa approval attachment
- dws oa approval create-instance
- dws oa approval detail
- dws oa approval ding-info
