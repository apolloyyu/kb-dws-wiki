# dws attendance check record

kind: command
completeness: full
usage: dws attendance check record
description: 查询打卡流水
example: dws attendance check record --users userId1 --start 2026-04-01 --end 2026-04-30
source: internal/helpers/attendance.go:742
visible_flags: 3

## Flags
- --users <String>: 用户 ID 列表，逗号分隔 (必填)
- --start <String>: 起始日期，格式 YYYY-MM-DD (必填)
- --end <String>: 结束日期，格式 YYYY-MM-DD，不超过 1 个月 (必填)

## Related
- dws attendance check result
