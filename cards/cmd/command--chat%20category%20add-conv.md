# dws chat category add-conv

kind: command
completeness: full
usage: dws chat category add-conv
description: 将会话移动到指定的自定义分组中
example: dws chat category add-conv --conversation-id <openConversationId> --category-ids 123,456
source: internal/helpers/chat.go:5937
visible_flags: 2

## Flags
- --conversation-id <String>: 会话 openConversationId (必填)
- --category-ids <String> required: 目标分组 ID 列表，逗号分隔 (必填)

## Related
- dws chat category batch-info
- dws chat category create
- dws chat category create-smart
- dws chat category delete
- dws chat category list
- dws chat category list-by-conv
