# dws contact org apply-block

kind: command
completeness: partial
usage: dws contact org apply-block
description: Block (blacklist) a join-enterprise application and its applicant with a reason.
use_when: When the user explicitly asks to blacklist an applicant, understanding later applications are also rejected.
source: internal/helpers/contact.go:3294
visible_flags: 0
partial_reason: unverified_usage,unverified_flags

## Flags
- none

## Related
- dws contact org apply-approve
- dws contact org apply-list
- dws contact org apply-reject
- dws contact org apply-remove
- dws contact org create
- dws contact org invite-audit
