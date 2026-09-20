# dws attendance +get-class

kind: shortcut
completeness: full
usage: dws attendance +get-class
description: 根据班次 ID 查询班次详情
source: internal/shortcut/attendance/attendance.go:1339
visible_flags: 1

## Flags
- --class-id <Int>: --class-id 必须大于 0，表示班次 ID

## Related
- dws attendance +boss-check
- dws attendance +calculate-approve-duration
- dws attendance +check-companion-schedules
- dws attendance +check-record
- dws attendance +check-result
- dws attendance +create-class
