# dws aitable table update

kind: command
completeness: full
description: Update a datasheet's name or other metadata.
use_when: When the agent needs to rename a datasheet without altering its contents.
source: internal/helpers/aitable.go:1897
visible_flags: 3

## Flags
- --base-id <String>: 目标 Base ID (必填)
- --name <String>: 新名称，1-50 字符 (必填)
- --desc <String>: 备注文本

## Related
- dws aitable table create
- dws aitable table delete
- dws aitable table get
- dws aitable table list
