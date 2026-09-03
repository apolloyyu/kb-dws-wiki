# dws attendance schedule get

kind: command
completeness: full
usage: dws attendance schedule get
description: 获取指定用户的排班记录
example: dws attendance schedule get --users user001,user002 --start 2026-04-01 --end 2026-04-30
source: internal/helpers/attendance.go:4387
visible_flags: 3

## Flags
- --users <String>: 用户ID列表，逗号分隔（必填）
- --start <String>: 开始日期，格式 YYYY-MM-DD 或 YYYY-MM-DD HH:mm:ss（必填）
- --end <String>: 结束日期，格式 YYYY-MM-DD 或 YYYY-MM-DD HH:mm:ss（必填）

## Related
- dws attendance schedule import
