# dws contact dept list-members

kind: command
completeness: full
description: List members of a specific department by department ID.
use_when: When the agent needs the roster of a department to target communication or build a team overview.
source: internal/helpers/contact.go:1266
visible_flags: 1

## Flags
- --id <String>: 角色 ID (必填)

## Related
- dws contact dept create
- dws contact dept get-info
- dws contact dept list-children
- dws contact dept search
- dws contact dept update
