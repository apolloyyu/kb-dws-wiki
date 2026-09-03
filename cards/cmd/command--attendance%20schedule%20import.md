# dws attendance schedule import

kind: command
completeness: full
description: 导入排班记录到排班制考勤组
source: internal/helpers/attendance.go:4268
visible_flags: 3

## Flags
- --groupId <String>: 考勤组ID（必填）
- --scheduleVOS <String>: 排班记录 JSON 数组（必填）
- --user-say-yes <Bool>: 用户已确认，跳过交互式确认提示（Agent 调用时传 true 前必须完成用户二次确认）

## Related
- dws attendance schedule get
