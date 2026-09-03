# dws oa approval list-pending

kind: command
completeness: full
description: List approval process instances currently awaiting action from the current user.
use_when: When the agent surfaces "needs your approval" items in the user's inbox.
source: internal/helpers/oa.go:927
visible_flags: 0

## Flags
- none

## Related
- dws oa approval approve
- dws oa approval create-instance
- dws oa approval detail
- dws oa approval forecast-process
- dws oa approval form-schema
- dws oa approval list-by-admin
