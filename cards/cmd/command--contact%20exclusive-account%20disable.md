# dws contact exclusive-account disable

kind: command
completeness: partial
usage: dws contact exclusive-account disable
description: Disable a dedicated enterprise login account so it can no longer sign in.
use_when: When the user explicitly asks to suspend an enterprise account and has confirmed the staff user ID.
source: internal/helpers/contact.go:3537
visible_flags: 0
partial_reason: unverified_usage,unverified_flags

## Flags
- none

## Related
- dws contact exclusive-account enable
