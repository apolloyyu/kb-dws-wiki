# dws attendance +query-report-leave

kind: shortcut
completeness: full
description: 查询用户假期数据（仅管理员）
source: internal/shortcut/attendance/attendance.go:1875
visible_flags: 4

## Flags
- --users <StringSlice>: 目标用户 userId 列表，逗号分隔，最多 20 人
- --leave-names <StringSlice>: 假期类型名称列表，逗号分隔，不填则查询所有假期类型
- --start <String>: 开始时间 yyyy-MM-dd HH:mm:ss
- --end <String>: 结束时间 yyyy-MM-dd HH:mm:ss，跨度不超过 32 天

## Related
- dws attendance +boss-check
- dws attendance +check-record
- dws attendance +check-result
- dws attendance +create-class
- dws attendance +create-group
- dws attendance +get-adjustment-rule
