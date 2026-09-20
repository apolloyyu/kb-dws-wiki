# dws attendance +get-approve-template

kind: shortcut
completeness: full
usage: dws attendance +get-approve-template
description: 查询补卡/请假/加班/外出/出差审批提交链接
source: internal/shortcut/attendance/attendance.go:540
visible_flags: 1

## Flags
- --type <String>: 审批类型：repair-check/补卡、leave/请假、overtime/加班、travel/外出、out/出差（或 REPAIR_CHECK/LEAVE/OVERTIME/TRAVEL/OUT）

## Related
- dws attendance +boss-check
- dws attendance +calculate-approve-duration
- dws attendance +check-companion-schedules
- dws attendance +check-record
- dws attendance +check-result
- dws attendance +create-class
