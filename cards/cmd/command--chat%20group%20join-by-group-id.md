# dws chat group join-by-group-id

kind: command
completeness: full
usage: dws chat group join-by-group-id
description: 通过群号申请加入群聊
example: dws chat group join-by-group-id --group-id 123456
source: internal/helpers/chat.go:10394
visible_flags: 1

## Flags
- --group-id <String> required: 目标群 numeric groupId (必填)

## Related
- dws chat group audit-join-validation
- dws chat group bots
- dws chat group create
- dws chat group dismiss
- dws chat group get-by-group-id
- dws chat group get-info-by-invite-url
