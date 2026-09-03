# dws aitable field update

kind: command
completeness: full
description: Update a field's name, type, or options in a datasheet.
use_when: When the agent needs to rename a column or change its type/options without recreating it.
source: internal/helpers/aitable.go:1897
visible_flags: 3

## Flags
- --base-id <String>: 目标 Base ID (必填)
- --name <String>: 新名称，1-50 字符 (必填)
- --desc <String>: 备注文本

## Related
- dws aitable field create
- dws aitable field delete
- dws aitable field get
- dws aitable field list
- dws aitable field search-options
