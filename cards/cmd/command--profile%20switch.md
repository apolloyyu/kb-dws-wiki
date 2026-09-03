# dws profile switch

kind: command
completeness: full
description: 切换当前账号 profile
source: internal/app/profile_command.go:106
visible_flags: 2

## Flags
- --corpId <String>: 按 corpId 直接切换组织 profile
- --name <String>: 按组织名或 profile 名直接切换组织 profile

## Related
- dws profile list
- dws profile use
