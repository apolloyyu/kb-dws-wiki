# dws contact dept search

kind: command
completeness: full
description: Search departments in the organization's contact directory by keyword.
use_when: When the agent needs to resolve a department name to a department ID.
source: internal/helpers/contact.go:1043
visible_flags: 1

## Flags
- --query <String>: 搜索关键词 (必填)

## Related
- dws contact dept create
- dws contact dept get-info
- dws contact dept list-children
- dws contact dept list-members
- dws contact dept update
