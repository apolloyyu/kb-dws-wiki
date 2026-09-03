# dws contact ext-field delete

kind: command
completeness: partial
usage: dws contact ext-field delete
description: 删除自定义字段
example: dws contact ext-field delete --code "rank"
source: internal/helpers/contact.go:629
visible_flags: 2
partial_reason: unverified_flags

## Flags
- --code <String>: 自定义字段编码 (必填)
- --org-self-tag <String>: 字段类型：1 企业个性化字段，0 默认扩展字段

## Related
- dws contact ext-field create
- dws contact ext-field list
- dws contact ext-field update
