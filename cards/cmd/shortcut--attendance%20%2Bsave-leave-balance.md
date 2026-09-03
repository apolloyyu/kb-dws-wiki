# dws attendance +save-leave-balance

kind: shortcut
completeness: full
description: 设置员工假期余额（SET 覆盖，非累加）
source: internal/shortcut/attendance/attendance.go:2135
visible_flags: 6

## Flags
- --target <String>: 目标员工工号 userId
- --leave-code <String>: 假期编码
- --num <String>: 余额数量（如 8 天传 8，7.5 天传 7.5）
- --reason <String>: 变更原因，最长 100 字符
- --start <String>: 有效期开始日期 YYYY-MM-DD
- --end <String>: 有效期结束日期 YYYY-MM-DD

## Related
- dws attendance +boss-check
- dws attendance +check-record
- dws attendance +check-result
- dws attendance +create-class
- dws attendance +create-group
- dws attendance +get-adjustment-rule
