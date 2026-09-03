# dws attendance report query-leave

kind: command
completeness: full
description: 查询用户假期数据
source: internal/helpers/attendance.go:3591
visible_flags: 4

## Flags
- --users <String>: 目标用户 userID 列表，逗号分隔，最多 20 人（必填）
- --leave-names <String>: 假期类型名称列表，逗号分隔，不填则查询所有假期类型（选填）
- --start <String>: 开始日期，格式 yyyy-MM-dd HH:mm:ss（必填）
- --end <String>: 结束日期，格式 yyyy-MM-dd HH:mm:ss（必填）

## Related
- dws attendance report columns
- dws attendance report query-data
