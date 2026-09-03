# dws contact label create

kind: command
completeness: partial
usage: dws contact label create
description: 创建角色或角色组
example: dws contact label create --name "管理员" --type role --parent-id 12345
source: internal/helpers/contact.go:228
visible_flags: 3
partial_reason: unverified_flags

## Flags
- --name <String>: 角色或角色组名称 (必填)
- --type <String>: 创建类型 (必填)：role 角色（需 --parent-id 指定所属角色组），group 角色组（挂在根层级）
- --parent-id <String>: 所属角色组 ID（--type role 时必填，正整数）

## Related
- dws contact label add-members
- dws contact label delete
- dws contact label get
- dws contact label list
- dws contact label list-members
- dws contact label remove-members
