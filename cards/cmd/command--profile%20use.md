# dws profile use

kind: command
completeness: full
usage: dws profile use [profile-selector|-]
description: 切换当前账号 profile（兼容 profile switch）
example: dws profile use <corpId>
source: internal/app/profile_command.go:88
visible_flags: 2

## Flags
- --corpId <String>: 按 corpId 直接切换组织 profile
- --name <String>: 按组织名或 profile 名直接切换组织 profile

## Related
- dws profile list
- dws profile switch
