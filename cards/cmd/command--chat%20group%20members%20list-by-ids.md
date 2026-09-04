# dws chat group members list-by-ids

kind: command
completeness: full
usage: dws chat group members list-by-ids
description: 根据成员 ID 批量查询群成员详情
example: dws chat group members list-by-ids --id <openConversationId> --users openDingTalkId1,openDingTalkId2
source: internal/helpers/chat.go:10573
visible_flags: 2

## Flags
- --id <String> required: 群 ID / openConversationId (必填)
- --users <String> required: 成员 openDingTalkId 列表，逗号分隔 (必填)

## Related
- dws chat group members add
- dws chat group members add-bot
- dws chat group members remove
- dws chat group members remove-bot
