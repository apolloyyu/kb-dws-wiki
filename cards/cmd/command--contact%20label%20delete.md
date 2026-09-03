# dws contact label delete

kind: command
completeness: partial
usage: dws contact label delete
description: 删除角色或角色组
example: dws contact label delete --id 12345
source: internal/helpers/contact.go:349
visible_flags: 1
partial_reason: unverified_flags

## Flags
- --id <String>: 要删除的角色或角色组 ID (必填)

## Related
- dws contact label add-members
- dws contact label create
- dws contact label get
- dws contact label list
- dws contact label list-members
- dws contact label remove-members
