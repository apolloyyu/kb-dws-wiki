# dws contact ext-field update

kind: command
completeness: full
description: 修改角色名称
source: internal/helpers/contact.go:309
visible_flags: 2

## Flags
- --id <String>: 角色 ID (必填)
- --name <String>: 角色新名称 (必填)

## Related
- dws contact ext-field create
- dws contact ext-field delete
- dws contact ext-field list
