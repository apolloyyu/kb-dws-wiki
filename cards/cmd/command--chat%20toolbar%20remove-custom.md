# dws chat toolbar remove-custom

kind: command
completeness: full
description: 删除自定义快捷栏入口
source: internal/helpers/chat/toolbar_remove_custom.go:37
visible_flags: 3

## Flags
- --conversation-id <String> required: 会话 openConversationId
- --shortcut-id <Int64> required: 自定义入口 ID
- --yes <Bool>: 确认执行删除操作

## Related
- dws chat toolbar add
- dws chat toolbar create-custom
- dws chat toolbar hide
- dws chat toolbar list
- dws chat toolbar sort
- dws chat toolbar update-custom
