# dws attendance rules

kind: command
completeness: full
description: Query the attendance group the user belongs to along with its attendance rules (schedule, locations, shifts).
use_when: When the agent needs to know the user's expected work schedule or attendance policies before interpreting records.
source: internal/helpers/attendance.go:2957
visible_flags: 1

## Flags
- --date <String>: 考勤日期，格式 YYYY-MM-DD 或 yyyy-MM-dd HH:mm:ss (必填)

## Related
- dws attendance boss-check
- dws attendance summary
