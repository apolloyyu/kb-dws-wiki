# dws aitable table get

kind: command
completeness: partial
usage: dws aitable table get
description: List datasheets within a Base, returning table IDs and names.
example: dws aitable table get --base-id BASE_ID
use_when: When the agent needs to resolve a table name to an ID inside a known Base.
source: internal/helpers/aitable.go:2052
visible_flags: 2
partial_reason: unverified_flags

## Flags
- --base-id <String>: 所属 Base ID（通过 base list / base search 获取）(必填)
- --table-ids <String>: 待获取详情的 Table ID 列表（通过 base get 获取），逗号分隔，单次最多 10 个；不传则默认返回当前 Base 下全部表。建议优先显式传入，以控制返回体大小，避免上下文突增

## Related
- dws aitable table create
- dws aitable table delete
- dws aitable table list
- dws aitable table update
