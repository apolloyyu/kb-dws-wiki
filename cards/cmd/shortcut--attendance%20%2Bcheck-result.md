# dws attendance +check-result

kind: shortcut
completeness: full
description: 查询用户打卡结果（迟到/早退/缺卡等）
source: internal/shortcut/attendance/attendance.go:171
visible_flags: 5

## Flags
- --users <StringSlice>: --users 不能为空，用户 ID 不能重复，最多 100 个，逗号分隔
- --start <String>: --start 必须是 YYYY-MM-DD
- --end <String>: --end 必须是 YYYY-MM-DD，不能早于 --start，且与 --start 跨度不超过 1 个月
- --offset <Int>: —
- --limit <Int>: —

## Related
- dws attendance +boss-check
- dws attendance +check-record
- dws attendance +create-class
- dws attendance +create-group
- dws attendance +get-adjustment-rule
- dws attendance +get-approve-template
