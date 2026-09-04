# dws chat category delete

kind: command
completeness: full
usage: dws chat category delete
description: 删除用户自定义会话分组
example: dws chat category delete --category-id <分组ID>
source: internal/helpers/chat.go:6028
visible_flags: 1

## Flags
- --category-id <Int64>: 会话分组 ID (必填)

## Related
- dws chat category add-conv
- dws chat category batch-info
- dws chat category create
- dws chat category create-smart
- dws chat category list
- dws chat category list-by-conv
