# dws attendance +check-companion-schedules

kind: shortcut
completeness: full
usage: dws attendance +check-companion-schedules
description: 校验出差/外出同行人的班次是否允许一起提交
source: internal/shortcut/attendance/attendance.go:867
visible_flags: 5

## Flags
- --approve-type <Int>: 审批类型，--approve-type 只能为 1（出差）或 2（外出）
- --starts <StringSlice>: 申请时间段开始时间列表，不能为空，YYYY-MM-DD 或 yyyy-MM-dd HH:mm:ss；与 --ends 按位置一一对应
- --ends <StringSlice>: 申请时间段结束时间列表，不能为空，格式同 --starts；与 --starts 数量必须一致
- --principal-users <StringSlice>: 同行人员工 userId 列表，逗号分隔
- --duration-unit <String>: —

## Related
- dws attendance +boss-check
- dws attendance +calculate-approve-duration
- dws attendance +check-record
- dws attendance +check-result
- dws attendance +create-class
- dws attendance +create-group
