# dws auth reset

kind: command
completeness: partial
usage: dws auth reset
description: 重置认证信息（清除本地 Token，触发重新授权）
source: internal/app/auth_command.go:1016
visible_flags: 0
partial_reason: unverified_flags

## Flags
- none

## Related
- dws auth exchange
- dws auth export
- dws auth import
- dws auth login
- dws auth logout
- dws auth migrate-keychain
