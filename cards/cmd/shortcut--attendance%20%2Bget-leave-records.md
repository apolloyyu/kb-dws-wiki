# dws attendance +get-leave-records

kind: shortcut
completeness: full
description: 查询指定员工的假期余额变更记录
source: internal/shortcut/attendance/attendance.go:1981
visible_flags: 4

## Flags
- --user <String>: 目标员工 userId
- --leave-code <String>: 假期规则 code（不传则查询所有假期）
- --start <String>: 查询开始日期 YYYY-MM-DD
- --end <String>: 查询结束日期 YYYY-MM-DD

## Related
- dws attendance +boss-check
- dws attendance +check-record
- dws attendance +check-result
- dws attendance +create-class
- dws attendance +create-group
- dws attendance +get-adjustment-rule
