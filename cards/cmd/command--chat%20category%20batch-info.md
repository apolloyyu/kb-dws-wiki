# dws chat category batch-info

kind: command
completeness: full
description: 批量拉取用户自定义会话分组信息
source: internal/helpers/chat.go:6103
visible_flags: 1

## Flags
- --category-ids <String> required: 分组 ID 列表，逗号分隔 (必填)

## Related
- dws chat category add-conv
- dws chat category create
- dws chat category create-smart
- dws chat category delete
- dws chat category list
- dws chat category list-by-conv
