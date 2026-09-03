# dws attendance report query-data

kind: command
completeness: full
usage: dws attendance report query-data
description: 根据字段查询考勤数据
example: dws attendance report query-data
source: internal/helpers/attendance.go:3508
visible_flags: 4

## Flags
- --users <String>: 目标用户 userID 列表，逗号分隔，最多 20 人（必填）
- --columns <String>: 字段 ID 列表，逗号分隔，可通过 report columns 获取（必填）
- --start <String>: 开始日期，格式 yyyy-MM-dd HH:mm:ss（必填）
- --end <String>: 结束日期，格式 yyyy-MM-dd HH:mm:ss（必填）

## Related
- dws attendance report columns
- dws attendance report query-leave
