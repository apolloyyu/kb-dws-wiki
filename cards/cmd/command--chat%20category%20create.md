# dws chat category create

kind: command
completeness: full
usage: dws chat category create
description: 创建用户自定义会话分组
example: dws chat category create --title "工作群"
source: internal/helpers/chat.go:5979
visible_flags: 1

## Flags
- --title <String> required: 分组名称，最多 15 个字符 (必填)

## Related
- dws chat category add-conv
- dws chat category batch-info
- dws chat category create-smart
- dws chat category delete
- dws chat category list
- dws chat category list-by-conv
