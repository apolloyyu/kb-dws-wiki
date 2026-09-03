# dws aitable field get

kind: command
completeness: full
description: Retrieve field definitions for a datasheet, including type, options, and order.
use_when: When the agent needs the field schema before constructing record payloads or queries.
source: internal/helpers/aitable.go:1812
visible_flags: 1

## Flags
- --base-id <String>: Base 唯一标识。优先使用 base search / base list 返回值 (必填)

## Related
- dws aitable field create
- dws aitable field delete
- dws aitable field list
- dws aitable field search-options
- dws aitable field update
