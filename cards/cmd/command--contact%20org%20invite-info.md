# dws contact org invite-info

kind: command
completeness: full
usage: dws contact org invite-info
description: Fetch the enterprise invite link, invite code, join switches, and audit type.
example: dws contact org invite-info
use_when: When the user asks for the invite link/QR code or wants to inspect current join settings.
source: internal/helpers/contact.go:3064
visible_flags: 0

## Flags
- none

## Related
- dws contact org apply-approve
- dws contact org apply-block
- dws contact org apply-list
- dws contact org apply-reject
- dws contact org apply-remove
- dws contact org create
