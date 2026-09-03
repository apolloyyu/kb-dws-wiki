# dws chat toolbar list

kind: command
completeness: full
usage: dws chat toolbar list
description: 查询会话快捷栏入口列表
example: dws chat toolbar list --conversation-id <cid>
source: internal/helpers/chat/toolbar_list.go:23
visible_flags: 1

## Flags
- --conversation-id <String> required: 会话 openConversationId

## Related
- dws chat toolbar add
- dws chat toolbar create-custom
- dws chat toolbar hide
- dws chat toolbar remove-custom
- dws chat toolbar sort
- dws chat toolbar update-custom
