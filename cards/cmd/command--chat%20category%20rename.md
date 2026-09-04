# dws chat category rename

kind: command
completeness: full
usage: dws chat category rename
description: 更新用户自定义会话分组的名称
example: dws chat category rename --category-id <分组ID> --title "新名称"
source: internal/helpers/chat.go:6084
visible_flags: 2

## Flags
- --category-id <Int64>: 会话分组 ID (必填)
- --title <String> required: 新的分组名称，最多 15 个字符 (必填)

## Related
- dws chat category add-conv
- dws chat category batch-info
- dws chat category create
- dws chat category create-smart
- dws chat category delete
- dws chat category list
