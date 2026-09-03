# dws chat group-role add

kind: command
completeness: full
description: 添加群成员
source: internal/helpers/chat.go:3185
visible_flags: 2

## Flags
- --id <String> required: 群 ID / openconversation_id (必填)
- --users <String> required: 要添加的用户 userId 或 openDingTalkId（可混传），逗号分隔 (必填)

## Related
- dws chat group-role list
- dws chat group-role query-user
- dws chat group-role remove
- dws chat group-role remove-user
- dws chat group-role set-user
- dws chat group-role update
