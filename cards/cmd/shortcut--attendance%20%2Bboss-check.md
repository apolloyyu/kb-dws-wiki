# dws attendance +boss-check

kind: shortcut
completeness: full
description: BOSS 改签打卡记录（管理员修改打卡时间/结果）
source: internal/shortcut/attendance/attendance.go:2281
visible_flags: 6

## Flags
- --plan-id <String>: 排班 ID（与 --result-id 二选一，可由 +get-schedule 获取 id）
- --result-id <String>: 打卡结果 ID（与 --plan-id 二选一，优先使用）
- --time <String>: 新打卡时间 yyyy-MM-dd HH:mm
- --result <String>: —
- --absent-min <Int>: 缺勤时长（分钟），异常结果时传值
- --remark <String>: 备注，最长 500 字符

## Related
- dws attendance +check-record
- dws attendance +check-result
- dws attendance +create-class
- dws attendance +create-group
- dws attendance +get-adjustment-rule
- dws attendance +get-approve-template
