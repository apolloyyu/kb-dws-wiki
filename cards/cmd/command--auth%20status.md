# dws auth status

kind: command
completeness: partial
usage: dws auth status
description: 查看认证状态
example: dws auth status
source: internal/app/auth_command.go:552
visible_flags: 2
partial_reason: unverified_flags

## Flags
- --profile <String>: 指定组织或账号：corpId、corpName、corpId:userId、corpId:userName、corpName:userId、corpName:userName 或本地 profile 名
- --readonly <Bool>: 只读本地登录态，不获取认证锁、不刷新、不迁移或修复

## Related
- dws auth exchange
- dws auth export
- dws auth import
- dws auth login
- dws auth logout
- dws auth migrate-keychain
