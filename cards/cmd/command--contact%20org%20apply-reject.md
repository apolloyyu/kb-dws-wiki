# dws contact org apply-reject

kind: command
completeness: partial
usage: dws contact org apply-reject
description: Reject a join-enterprise application by application ID with a reason.
use_when: When the user explicitly asks to decline an application and provide the rejection reason.
source: internal/helpers/contact.go:3254
visible_flags: 0
partial_reason: unverified_usage,unverified_flags

## Flags
- none

## Related
- dws contact org apply-approve
- dws contact org apply-block
- dws contact org apply-list
- dws contact org apply-remove
- dws contact org create
- dws contact org invite-audit
