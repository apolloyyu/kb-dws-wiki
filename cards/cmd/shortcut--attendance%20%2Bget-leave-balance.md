# dws attendance +get-leave-balance

kind: shortcut
completeness: full
description: 查询指定员工的假期余额
source: internal/shortcut/attendance/attendance.go:1955
visible_flags: 2

## Flags
- --users <StringSlice>: 目标员工 userId 列表，逗号分隔
- --leave-code <String>: 假期规则 code（不传则查询所有假期）

## Related
- dws attendance +boss-check
- dws attendance +check-record
- dws attendance +check-result
- dws attendance +create-class
- dws attendance +create-group
- dws attendance +get-adjustment-rule
