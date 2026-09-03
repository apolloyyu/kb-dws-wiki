# dws aitable dashboard update

kind: command
completeness: full
description: Update an existing dashboard's layout, widgets, or metadata.
use_when: When the agent adds, removes, or rearranges charts on an existing dashboard.
source: internal/helpers/aitable.go:1897
visible_flags: 3

## Flags
- --base-id <String>: 目标 Base ID (必填)
- --name <String>: 新名称，1-50 字符 (必填)
- --desc <String>: 备注文本

## Related
- dws aitable dashboard arrange
- dws aitable dashboard config-example
- dws aitable dashboard create
- dws aitable dashboard delete
- dws aitable dashboard get
