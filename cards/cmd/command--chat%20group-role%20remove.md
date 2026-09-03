# dws chat group-role remove

kind: command
completeness: full
description: 移除群成员
source: internal/helpers/chat.go:3237
visible_flags: 2

## Flags
- --id <String> required: 群 ID / openconversation_id (必填)
- --users <String> required: 要移除的用户 userId 列表，逗号分隔 (必填)

## Related
- dws chat group-role add
- dws chat group-role list
- dws chat group-role query-user
- dws chat group-role remove-user
- dws chat group-role set-user
- dws chat group-role update
