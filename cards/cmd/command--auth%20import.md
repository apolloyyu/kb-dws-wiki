# dws auth import

kind: command
completeness: partial
usage: dws auth import
description: 导入可迁移认证包
example: dws auth import -i dws-auth.tar.gz
source: internal/app/auth_command.go:890
visible_flags: 3
partial_reason: unverified_flags

## Flags
- --input (-i) <String>: 认证包输入路径
- --base64 <Bool>: 输入为 base64 编码的认证包
- --force <Bool>: 覆盖已有登录态

## Related
- dws auth exchange
- dws auth export
- dws auth login
- dws auth logout
- dws auth migrate-keychain
- dws auth reset
