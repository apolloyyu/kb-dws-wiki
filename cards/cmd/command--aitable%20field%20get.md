# dws aitable field get

kind: command
completeness: partial
usage: dws aitable field get
description: Retrieve field definitions for a datasheet, including type, options, and order.
example: dws aitable field get --base-id BASE_ID --table-id TABLE_ID
use_when: When the agent needs the field schema before constructing record payloads or queries.
source: internal/helpers/aitable.go:2323
visible_flags: 3
partial_reason: unverified_flags

## Flags
- --base-id <String>: Base ID（可通过 base list 获取）(必填)
- --table-id <String>: Table ID（可通过 base get 获取）(必填)
- --field-ids <String>: 待获取详情的字段 ID 列表（通过 table get 获取），逗号分隔；建议只传真正需要展开完整配置的字段，单次最多 10 个；不传则返回全部字段。建议优先显式传入，以控制返回体大小，避免上下文突增

## Related
- dws aitable field create
- dws aitable field delete
- dws aitable field list
- dws aitable field search-options
- dws aitable field update
