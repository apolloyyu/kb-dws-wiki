# dws chat group get-by-group-id

kind: command
completeness: full
usage: dws chat group get-by-group-id
description: 根据群号获取群聊信息
example: dws chat group get-by-group-id --group-id 12345678
source: internal/helpers/chat.go:6155
visible_flags: 1

## Flags
- --group-id <Int64> required: 群号 (必填，数字类型)

## Related
- dws chat group audit-join-validation
- dws chat group bots
- dws chat group create
- dws chat group dismiss
- dws chat group get-mute-config
- dws chat group invite-url
