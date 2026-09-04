# dws chat category list-by-conv

kind: command
completeness: partial
usage: dws chat category list-by-conv
description: 拉取指定会话所属的用户自定义会话分组
example: dws chat category list-by-conv --conversation-id <openConversationId>
source: internal/helpers/chat.go:6257
visible_flags: 1
partial_reason: unverified_flags

## Flags
- --conversation-id <String> required: 会话 openConversationId (必填)

## Related
- dws chat category add-conv
- dws chat category batch-info
- dws chat category create
- dws chat category create-smart
- dws chat category delete
- dws chat category list
