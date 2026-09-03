# dws contact label update-member-scope

kind: command
completeness: partial
usage: dws contact label update-member-scope
description: 修改角色管理范围
example: dws contact label update-member-scope --user user1 --id 12345 --depts 1,2
source: internal/helpers/contact.go:466
visible_flags: 3
partial_reason: unverified_flags

## Flags
- --user <String>: 成员 staffId / userId (必填)
- --id <String>: 角色 ID (必填)
- --depts <String>: 可管理部门 ID 列表，逗号分隔 (必填)

## Related
- dws contact label add-members
- dws contact label create
- dws contact label delete
- dws contact label get
- dws contact label list
- dws contact label list-members
