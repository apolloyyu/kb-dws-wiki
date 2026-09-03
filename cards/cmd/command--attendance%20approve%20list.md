# dws attendance approve list

kind: command
completeness: full
description: 查询用户审批单（补卡/加班/请假/出差外出）
source: internal/helpers/attendance.go:862
visible_flags: 4

## Flags
- --users <String>: 用户 ID 列表，逗号分隔 (必填)
- --types <String>: 审批类型，逗号分隔：overtime/trip/leave/patch (必填)
- --start <String>: 起始日期，格式 YYYY-MM-DD (必填)
- --end <String>: 结束日期，格式 YYYY-MM-DD (必填)

## Related
- dws attendance approve leave-check
- dws attendance approve leave-duration
- dws attendance approve leave-types
- dws attendance approve supply-check
- dws attendance approve supply-plans
- dws attendance approve templates
