# dws audit verify

kind: command
completeness: full
usage: dws audit verify
description: 校验审计日志哈希链完整性
source: internal/app/audit_command.go:196
visible_flags: 1

## Flags
- --file <String>: 指定审计文件路径（默认最新文件）

## Related
- dws audit export
- dws audit tail
