# dws chat category list-conversations

kind: command
completeness: full
usage: dws chat category list-conversations
description: 拉取指定自定义会话分组下的会话
example: dws chat category list-conversations --category-id <分组ID>
source: internal/helpers/chat.go:5935
visible_flags: 2

## Flags
- --category-id <Int> required: 会话分组 ID (必填)
- --exclude-muted <Bool>: 是否排除已设置免打扰的会话（默认 false）

## Related
- dws chat category add-conv
- dws chat category batch-info
- dws chat category create
- dws chat category create-smart
- dws chat category delete
- dws chat category list
