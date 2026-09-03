# dws contact label remove-members

kind: command
completeness: partial
usage: dws contact label remove-members
description: 移除成员角色
example: dws contact label remove-members --id 12345 --users user1,user2
source: internal/helpers/contact.go:421
visible_flags: 2
partial_reason: unverified_flags

## Flags
- --id <String>: 角色 ID 列表，逗号分隔 (必填)
- --users <String>: 成员 userId 列表，逗号分隔 (必填)

## Related
- dws contact label add-members
- dws contact label create
- dws contact label delete
- dws contact label get
- dws contact label list
- dws contact label list-members
