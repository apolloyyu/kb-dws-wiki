# dws attendance +import-schedule

kind: shortcut
completeness: full
usage: dws attendance +import-schedule
description: 导入排班记录到排班制考勤组
source: internal/shortcut/attendance/attendance.go:644
visible_flags: 2

## Flags
- --group-id <Int>: 考勤组 ID
- --schedules <String>: —

## Related
- dws attendance +boss-check
- dws attendance +check-record
- dws attendance +check-result
- dws attendance +create-class
- dws attendance +create-group
- dws attendance +get-adjustment-rule
