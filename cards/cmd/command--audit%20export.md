# dws audit export

kind: command
completeness: full
usage: dws audit export
description: 导出审计日志
source: internal/app/audit_command.go:128
visible_flags: 3

## Flags
- --since <String>: 起始日期 (YYYY-MM-DD)
- --until <String>: 截止日期 (YYYY-MM-DD)
- --format <String>: 输出格式: jsonl 或 csv

## Related
- dws audit tail
- dws audit verify
