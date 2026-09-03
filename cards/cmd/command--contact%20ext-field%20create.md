# dws contact ext-field create

kind: command
completeness: partial
usage: dws contact ext-field create
description: 创建自定义字段
example: dws contact ext-field create --name "职级"
source: internal/helpers/contact.go:536
visible_flags: 1
partial_reason: unverified_flags

## Flags
- --name <String>: 自定义字段显示名称 (必填)

## Related
- dws contact ext-field delete
- dws contact ext-field list
- dws contact ext-field update
