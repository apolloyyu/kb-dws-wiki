# dws contact label get

kind: command
completeness: full
usage: dws contact label get
description: 根据角色名称查询角色
example: dws contact label get --names "管理员"
source: internal/helpers/contact.go:1254
visible_flags: 1

## Flags
- --names <String>: 角色名称，逗号分隔 (必填)

## Related
- dws contact label add-members
- dws contact label create
- dws contact label delete
- dws contact label list
- dws contact label list-members
- dws contact label remove-members
