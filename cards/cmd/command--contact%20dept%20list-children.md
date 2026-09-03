# dws contact dept list-children

kind: command
completeness: full
usage: dws contact dept list-children
description: 查看子部门
example: dws contact dept list-children --dept 12345
source: internal/helpers/contact.go:1582
visible_flags: 1

## Flags
- --dept <String>: 部门 ID (必填)

## Related
- dws contact dept create
- dws contact dept get-info
- dws contact dept list-members
- dws contact dept search
- dws contact dept update
