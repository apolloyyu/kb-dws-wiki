# dws aitable chart update

kind: command
completeness: full
description: Update an existing chart's configuration (type, dimensions, metrics, style).
use_when: When the agent iterates on a chart's visualization after reviewing the initial result.
source: internal/helpers/aitable.go:1897
visible_flags: 3

## Flags
- --base-id <String>: 目标 Base ID (必填)
- --name <String>: 新名称，1-50 字符 (必填)
- --desc <String>: 备注文本

## Related
- dws aitable chart create
- dws aitable chart delete
- dws aitable chart get
- dws aitable chart widgets-example
