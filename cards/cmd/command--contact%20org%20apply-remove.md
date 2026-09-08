# dws contact org apply-remove

kind: command
completeness: partial
usage: dws contact org apply-remove
description: Delete a join-enterprise application record permanently.
use_when: When the user explicitly asks to remove an application record and accepts it cannot be recovered.
source: internal/helpers/contact.go:3337
visible_flags: 0
partial_reason: unverified_usage,unverified_flags

## Flags
- none

## Related
- dws contact org apply-approve
- dws contact org apply-block
- dws contact org apply-list
- dws contact org apply-reject
- dws contact org create
- dws contact org invite-audit
