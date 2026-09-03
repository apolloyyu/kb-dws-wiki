# dws contact dept get-info

kind: command
completeness: full
usage: dws contact dept get-info
description: 获取部门详情（部门ID、名称、人数）
example: dws contact dept get-info --dept 12345
source: internal/helpers/contact.go:1628
visible_flags: 1

## Flags
- --dept <String>: 部门 ID (必填)

## Related
- dws contact dept create
- dws contact dept list-children
- dws contact dept list-members
- dws contact dept search
- dws contact dept update
