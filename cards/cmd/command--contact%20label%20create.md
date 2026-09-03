# dws contact label create

kind: command
completeness: full
description: 创建部门
source: internal/helpers/contact.go:180
visible_flags: 3

## Flags
- --name <String>: 部门名称 (必填)
- --parent <String>: 父部门 ID（可选，不传默认根部门）
- --create-dept-group <Bool>: 是否创建部门群 (必填，需显式传 true 或 false)

## Related
- dws contact label add-members
- dws contact label delete
- dws contact label get
- dws contact label list-members
- dws contact label remove-members
- dws contact label update
