# dws contact label add-members

kind: command
completeness: full
description: 给成员添加角色
source: internal/helpers/contact.go:377
visible_flags: 2

## Flags
- --id <String>: 角色 ID 列表，逗号分隔 (必填)
- --users <String>: 成员 userId 列表，逗号分隔 (必填)

## Related
- dws contact label create
- dws contact label delete
- dws contact label get
- dws contact label list-members
- dws contact label remove-members
- dws contact label update
