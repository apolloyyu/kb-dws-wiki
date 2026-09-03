# dws attendance boss-check

kind: command
completeness: full
description: BOSS 改签打卡记录
source: internal/helpers/attendance.go:4817
visible_flags: 7

## Flags
- --plan-id <String>: 排班ID（与 --result-id 二选一）
- --result-id <String>: 打卡结果ID（与 --plan-id 二选一，优先使用）
- --time <String>: 新打卡时间，格式 yyyy-MM-dd HH:mm（可选）
- --result <String>: 打卡结果：Normal/TimesResultA/TimesResultB/TimesResultC/TimesResultD/TimesResultE/TimesResultF（可选）
- --absent-min <Int>: 缺勤时长（分钟）（可选）
- --remark <String>: 备注，最长500字符（可选）
- --user-say-yes <Bool>: 用户已确认，跳过交互式确认提示

## Related
- dws attendance rules
- dws attendance summary
