# dws aitable view delete

kind: command
completeness: full
usage: dws aitable view delete
description: Delete a view from a datasheet by view ID.
example: dws aitable view delete --base-id BASE_ID --table-id TABLE_ID --view-id VIEW_ID --yes
use_when: When the agent is cleaning up unused views.
source: internal/helpers/aitable.go:5112
visible_flags: 3

## Flags
- --base-id <String>: 所属 Base ID (必填)
- --table-id <String>: 所属 Table ID (必填)
- --view-id <String>: 要删除的 View ID (必填)

## Related
- dws aitable view create
- dws aitable view duplicate
- dws aitable view get
- dws aitable view list
- dws aitable view lock
- dws aitable view update
