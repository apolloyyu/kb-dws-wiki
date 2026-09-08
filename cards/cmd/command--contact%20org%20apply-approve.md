# dws contact org apply-approve

kind: command
completeness: partial
usage: dws contact org apply-approve
description: Approve a pending join-enterprise application by application ID.
use_when: When the user explicitly asks to accept an application after confirming it via `dws contact org apply-list`.
source: internal/helpers/contact.go:3215
visible_flags: 0
partial_reason: unverified_usage,unverified_flags

## Flags
- none

## Related
- dws contact org apply-block
- dws contact org apply-list
- dws contact org apply-reject
- dws contact org apply-remove
- dws contact org create
- dws contact org invite-audit
