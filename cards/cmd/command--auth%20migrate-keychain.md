# dws auth migrate-keychain

kind: command
completeness: full
usage: dws auth migrate-keychain
description: 将 macOS 系统 Keychain 登录态安全迁移到 file-DEK
source: internal/app/auth_command.go:670
visible_flags: 1

## Flags
- --to <String>: 目标密钥后端（当前仅支持 file-dek）

## Related
- dws auth exchange
- dws auth export
- dws auth import
- dws auth login
- dws auth logout
- dws auth reset
