# dws audit tail

kind: command
completeness: full
usage: dws audit tail
description: 查看最近的审计记录
source: internal/app/audit_command.go:67
visible_flags: 1

## Flags
- --lines (-n) <Int>: 显示最近 N 条记录

## Related
- dws audit export
- dws audit verify
