# dws attendance +get-complex-overtime-setting

kind: shortcut
completeness: full
usage: dws attendance +get-complex-overtime-setting
description: 查询员工在指定日期适用的复杂加班规则
source: internal/shortcut/attendance/attendance.go:989
visible_flags: 2

## Flags
- --users <StringSlice>: 员工 userId 列表，不能为空、不能重复，逗号分隔
- --work-date <String>: 规则生效日期，--work-date 如传入，必须为 YYYY-MM-DD 或 yyyy-MM-dd HH:mm:ss；不传时使用服务端当前时间

## Related
- dws attendance +boss-check
- dws attendance +calculate-approve-duration
- dws attendance +check-companion-schedules
- dws attendance +check-record
- dws attendance +check-result
- dws attendance +create-class
