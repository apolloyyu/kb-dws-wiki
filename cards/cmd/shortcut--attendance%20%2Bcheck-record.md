# dws attendance +check-record

kind: shortcut
completeness: full
description: 查询用户打卡流水（打卡时间/地点/定位方式）
source: internal/shortcut/attendance/attendance.go:287
visible_flags: 3

## Flags
- --users <StringSlice>: --users 不能为空，用户 ID 不能重复，逗号分隔
- --start <String>: --start 必须是 YYYY-MM-DD
- --end <String>: --end 必须是 YYYY-MM-DD，不能早于 --start，且与 --start 跨度不超过 1 个月

## Related
- dws attendance +boss-check
- dws attendance +check-result
- dws attendance +create-class
- dws attendance +create-group
- dws attendance +get-adjustment-rule
- dws attendance +get-approve-template
