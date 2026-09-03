# dws attendance +get-summary

kind: shortcut
completeness: full
description: 查询某个人的考勤统计摘要（周/月）
source: internal/shortcut/attendance/attendance.go:1597
visible_flags: 3

## Flags
- --user <String>: 钉钉用户 userId
- --date <String>: 查询日期 YYYY-MM-DD 或 yyyy-MM-dd HH:mm:ss
- --stats-type <String>: —

## Related
- dws attendance +boss-check
- dws attendance +check-record
- dws attendance +check-result
- dws attendance +create-class
- dws attendance +create-group
- dws attendance +get-adjustment-rule
