# dws aitable view get

kind: command
completeness: partial
usage: dws aitable view get
description: Retrieve view definitions for a datasheet, including filter, sort, and visible-field configuration.
example: dws aitable view get --base-id BASE_ID --table-id TABLE_ID
use_when: When the agent needs to understand or reuse a view's configuration before querying records through it.
source: internal/helpers/aitable.go:3778
visible_flags: 3
partial_reason: unverified_flags

## Flags
- --base-id <String>: 所属 Base ID (必填)
- --table-id <String>: 所属 Table ID (必填)
- --view-ids <String>: 待获取详情的 View ID 列表，逗号分隔，单次最多 10 个；不传则返回全部视图

## Related
- dws aitable view create
- dws aitable view delete
- dws aitable view duplicate
- dws aitable view list
- dws aitable view lock
- dws aitable view update
