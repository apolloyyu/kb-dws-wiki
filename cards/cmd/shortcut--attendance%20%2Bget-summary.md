# dws attendance +get-summary

kind: shortcut
completeness: full
usage: dws attendance +get-summary
description: 查询某个人的考勤统计摘要（周/月）
source: internal/shortcut/attendance/attendance.go:2103
visible_flags: 3

## Flags
- --user <String>: 钉钉用户 userId
- --date <String>: 查询日期 YYYY-MM-DD 或 yyyy-MM-dd HH:mm:ss
- --stats-type <String>: —

## Related
- dws attendance +boss-check
- dws attendance +calculate-approve-duration
- dws attendance +check-companion-schedules
- dws attendance +check-record
- dws attendance +check-result
- dws attendance +create-class
