# dws chat group user-settings set

kind: command
completeness: full
usage: dws chat group user-settings set
description: 批量更新当前用户的群会话设置
example: dws chat group user-settings set --items '[{"openConversationId":"cid1","top":true,"mute":false}]'
source: internal/helpers/chat.go:11267
visible_flags: 1

## Flags
- --items <String>: ...

## Related
- dws chat group user-settings query
