# dws chat category rename

kind: command
completeness: full
description: 更新群名称
source: internal/helpers/chat.go:3138
visible_flags: 2

## Flags
- --id <String> required: 群 ID / openconversation_id (必填)
- --name <String> required: 修改后的群名称 (必填)

## Related
- dws chat category add-conv
- dws chat category batch-info
- dws chat category create
- dws chat category create-smart
- dws chat category delete
- dws chat category list
