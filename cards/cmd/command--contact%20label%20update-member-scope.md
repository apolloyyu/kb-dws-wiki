# dws contact label update-member-scope

kind: command
completeness: full
description: 修改角色管理范围
source: internal/helpers/contact.go:466
visible_flags: 3

## Flags
- --user <String>: 成员 staffId / userId (必填)
- --id <String>: 角色 ID (必填)
- --depts <String>: 可管理部门 ID 列表，逗号分隔 (必填)

## Related
- dws contact label add-members
- dws contact label create
- dws contact label delete
- dws contact label get
- dws contact label list-members
- dws contact label remove-members
