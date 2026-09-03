# dws attendance +list-approve

kind: shortcut
completeness: full
description: 查询用户考勤审批单（补卡/加班/请假/出差外出）
source: internal/shortcut/attendance/attendance.go:375
visible_flags: 4

## Flags
- --users <StringSlice>: --users 不能为空，用户 ID 不能重复，逗号分隔
- --types <StringSlice>: --types 不能为空，映射后的审批类型不能重复；overtime/加班、trip/travel/出差/外出、leave/请假、patch/补卡
- --start <String>: --start 必须是 YYYY-MM-DD
- --end <String>: --end 必须是 YYYY-MM-DD，且不能早于 --start

## Related
- dws attendance +boss-check
- dws attendance +check-record
- dws attendance +check-result
- dws attendance +create-class
- dws attendance +create-group
- dws attendance +get-adjustment-rule
