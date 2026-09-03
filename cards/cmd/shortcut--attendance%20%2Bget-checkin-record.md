# dws attendance +get-checkin-record

kind: shortcut
completeness: full
usage: dws attendance +get-checkin-record
description: 查询指定员工一段时间内的签到记录
source: internal/shortcut/attendance/attendance.go:2185
visible_flags: 5

## Flags
- --operator-corp-id <String>: 操作者企业 ID
- --operator-staff-id <String>: 操作者员工 ID
- --staff-ids <StringSlice>: 目标员工 ID 列表，逗号分隔，最多 100 人
- --start <String>: 开始时间 yyyy-MM-dd HH:mm:ss
- --end <String>: 结束时间 yyyy-MM-dd HH:mm:ss，跨度最多 7 天

## Related
- dws attendance +boss-check
- dws attendance +check-record
- dws attendance +check-result
- dws attendance +create-class
- dws attendance +create-group
- dws attendance +get-adjustment-rule
