# dws contact dept update

kind: command
completeness: partial
usage: dws contact dept update
description: 更新部门信息
example: dws contact dept update --dept 12345 --name "新部门名"
source: internal/helpers/contact.go:677
visible_flags: 3
partial_reason: unverified_flags

## Flags
- --dept <String>: 部门 ID (必填)
- --name <String>: 新部门名称 (必填)
- --parent <String>: 新父部门 ID（可选）

## Related
- dws contact dept create
- dws contact dept get-info
- dws contact dept list-children
- dws contact dept list-members
- dws contact dept search
