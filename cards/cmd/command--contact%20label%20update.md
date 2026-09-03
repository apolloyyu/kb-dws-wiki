# dws contact label update

kind: command
completeness: partial
usage: dws contact label update
description: 修改角色名称
example: dws contact label update --id 12345 --name "新名称"
source: internal/helpers/contact.go:309
visible_flags: 2
partial_reason: unverified_flags

## Flags
- --id <String>: 角色 ID (必填)
- --name <String>: 角色新名称 (必填)

## Related
- dws contact label add-members
- dws contact label create
- dws contact label delete
- dws contact label get
- dws contact label list
- dws contact label list-members
