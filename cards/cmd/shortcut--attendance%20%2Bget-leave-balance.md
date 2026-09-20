# dws attendance +get-leave-balance

kind: shortcut
completeness: full
usage: dws attendance +get-leave-balance
description: 查询指定员工的假期余额
source: internal/shortcut/attendance/attendance.go:2461
visible_flags: 2

## Flags
- --users <StringSlice>: 目标员工 userId 列表，逗号分隔
- --leave-code <String>: 假期规则 code（不传则查询所有假期）

## Related
- dws attendance +boss-check
- dws attendance +calculate-approve-duration
- dws attendance +check-companion-schedules
- dws attendance +check-record
- dws attendance +check-result
- dws attendance +create-class
