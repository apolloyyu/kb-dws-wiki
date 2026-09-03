# dws contact label list-members

kind: command
completeness: full
usage: dws contact label list-members
description: 查询角色下的成员
example: dws contact label list-members --id 12345
source: internal/helpers/contact.go:1266
visible_flags: 1

## Flags
- --id <String>: 角色 ID (必填)

## Related
- dws contact label add-members
- dws contact label create
- dws contact label delete
- dws contact label get
- dws contact label list
- dws contact label remove-members
