# dws attendance +get-schedule

kind: shortcut
completeness: full
description: 获取指定用户一段时间内的排班记录
source: internal/shortcut/attendance/attendance.go:559
visible_flags: 3

## Flags
- --users <StringSlice>: --users 不能为空，用户 ID 不能重复，逗号分隔
- --start <String>: --start 必须是 YYYY-MM-DD 或 yyyy-MM-dd HH:mm:ss
- --end <String>: --end 必须是 YYYY-MM-DD 或 yyyy-MM-dd HH:mm:ss，且不能早于 --start

## Related
- dws attendance +boss-check
- dws attendance +check-record
- dws attendance +check-result
- dws attendance +create-class
- dws attendance +create-group
- dws attendance +get-adjustment-rule
