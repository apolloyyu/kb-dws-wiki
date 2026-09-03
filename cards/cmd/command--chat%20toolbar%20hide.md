# dws chat toolbar hide

kind: command
completeness: full
description: 将入口从快捷栏可见区隐藏
source: internal/helpers/chat/toolbar_hide.go:25
visible_flags: 2

## Flags
- --conversation-id <String> required: 会话 openConversationId
- --shortcut-ids <String> required: 入口 ID 列表（逗号分隔）

## Related
- dws chat toolbar add
- dws chat toolbar create-custom
- dws chat toolbar list
- dws chat toolbar remove-custom
- dws chat toolbar sort
- dws chat toolbar update-custom
