# dws auth logout

kind: command
completeness: full
description: 清除认证信息（默认退出所有组织）
source: internal/app/auth_command.go:504
visible_flags: 1

## Flags
- --profile <String>: 指定组织或账号：corpId、corpName、corpId:userId、corpId:userName、corpName:userId、corpName:userName 或本地 profile 名

## Related
- dws auth exchange
- dws auth login
- dws auth migrate-keychain
- dws auth reset
- dws auth status
