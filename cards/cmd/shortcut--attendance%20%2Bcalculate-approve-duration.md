# dws attendance +calculate-approve-duration

kind: shortcut
completeness: partial
usage: dws attendance +calculate-approve-duration
description: 计算加班/请假/外出等考勤审批时长
source: internal/shortcut/attendance/attendance.go:600
visible_flags: 16
partial_reason: too_many_flags:16

## Flags
- --biz-type <Int>: 审批业务类型，--biz-type 必须在 1 到 8 之间：1-加班，2-普通审批，3-请假，4-补卡，5-外出，6-换班，7-考勤证明，8-单次外出
- --approve-biz-type <String>: 普通审批场景的原始审批子类型，用于区分外出、出差等；不确定时不传
- --duration-mode <Int>: 时长模式，--duration-mode 必须在 1 到 5 之间：1-天，2-半天，3-小时，4-半小时，5-分钟
- --start <String>: 开始时间，--start 必须为 YYYY-MM-DD 或 yyyy-MM-dd HH:mm:ss
- --end <String>: 结束时间，--end 必须为 YYYY-MM-DD 或 yyyy-MM-dd HH:mm:ss，且不得早于 --start
- --half-start <String>: —
- --half-end <String>: —
- --push-tag <String>: 可选审批业务标签
- … 8 more; use dwsdoc cmd/short for full flags

## Related
- dws attendance +boss-check
- dws attendance +check-companion-schedules
- dws attendance +check-record
- dws attendance +check-result
- dws attendance +create-class
- dws attendance +create-group
