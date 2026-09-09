# dws contact exclusive-account enable

kind: command
completeness: partial
usage: dws contact exclusive-account enable
description: Re-enable a previously disabled dedicated enterprise login account.
use_when: When the user explicitly asks to restore an enterprise account's ability to sign in.
source: internal/helpers/contact.go:3572
visible_flags: 0
partial_reason: unverified_usage,unverified_flags

## Flags
- none

## Related
- dws contact exclusive-account disable
