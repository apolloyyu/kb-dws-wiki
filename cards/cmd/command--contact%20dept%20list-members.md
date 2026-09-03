# dws contact dept list-members

kind: command
completeness: full
usage: dws contact dept list-members
description: List members of a specific department by department ID.
example: dws contact dept list-members --depts 12345,67890
use_when: When the agent needs the roster of a department to target communication or build a team overview.
source: internal/helpers/contact.go:1674
visible_flags: 1

## Flags
- --depts <String>: 部门 ID 列表 (必填)

## Related
- dws contact dept create
- dws contact dept get-info
- dws contact dept list-children
- dws contact dept search
- dws contact dept update
