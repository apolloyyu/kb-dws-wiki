# dws contact label add-members

kind: command
completeness: partial
usage: dws contact label add-members
description: 给成员添加角色
example: dws contact label add-members --id 12345 --users user1,user2
source: internal/helpers/contact.go:377
visible_flags: 2
partial_reason: unverified_flags

## Flags
- --id <String>: 角色 ID 列表，逗号分隔 (必填)
- --users <String>: 成员 userId 列表，逗号分隔 (必填)

## Related
- dws contact label create
- dws contact label delete
- dws contact label get
- dws contact label list
- dws contact label list-members
- dws contact label remove-members
