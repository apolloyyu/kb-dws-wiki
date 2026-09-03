# dws attendance +query-report-data

kind: shortcut
completeness: full
usage: dws attendance +query-report-data
description: 根据字段查询考勤报表数据（仅管理员）
source: internal/shortcut/attendance/attendance.go:1803
visible_flags: 4

## Flags
- --users <StringSlice>: 目标用户 userId 列表，逗号分隔，最多 20 人
- --columns <StringSlice>: 字段 ID 列表，逗号分隔（可用 +list-report-columns 获取）
- --start <String>: 开始时间 yyyy-MM-dd HH:mm:ss
- --end <String>: 结束时间 yyyy-MM-dd HH:mm:ss，跨度不超过 32 天

## Related
- dws attendance +boss-check
- dws attendance +check-record
- dws attendance +check-result
- dws attendance +create-class
- dws attendance +create-group
- dws attendance +get-adjustment-rule
