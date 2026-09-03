# dws chat group list-my-groups

kind: command
completeness: full
usage: dws chat group list-my-groups
description: 拉取我创建/管理的群
example: dws chat group list-my-groups
source: internal/helpers/chat.go:9325
visible_flags: 3

## Flags
- --role <String>: 角色过滤: OWNER(仅群主) / ADMIN(仅管理员)，不传返回全部
- --limit <Int>: 最多返回群数量，不传返回全部
- --exclude-muted <Bool>: 是否排除已设置免打扰的群聊（默认 false）

## Related
- dws chat group audit-join-validation
- dws chat group bots
- dws chat group create
- dws chat group dismiss
- dws chat group get-by-group-id
- dws chat group get-mute-config
