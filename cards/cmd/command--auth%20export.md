# dws auth export

kind: command
completeness: partial
usage: dws auth export
description: 导出可迁移认证包
example: dws auth export -o dws-auth.tar.gz
source: internal/app/auth_command.go:816
visible_flags: 2
partial_reason: unverified_flags

## Flags
- --output (-o) <String>: 认证包输出路径
- --base64 <Bool>: 将认证包编码为 base64，便于复制粘贴

## Related
- dws auth exchange
- dws auth import
- dws auth login
- dws auth logout
- dws auth migrate-keychain
- dws auth reset
