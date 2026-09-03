# dws chat group user-settings query

kind: command
completeness: full
usage: dws chat group user-settings query
description: 批量查询当前用户的群会话设置
example: dws chat group user-settings query --groups cid1,cid2
source: internal/helpers/chat.go:11017
visible_flags: 1

## Flags
- --groups <String>: 群会话 openConversationId 列表，逗号分隔，最多 100 个 (必填)

## Related
- dws chat group user-settings set
