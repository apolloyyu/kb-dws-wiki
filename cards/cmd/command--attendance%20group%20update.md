# dws attendance group update

kind: command
completeness: full
usage: dws attendance group update
description: 更新考勤组配置（仅修改需要变更的字段）
example: dws attendance group update --group-id 123456 --name "研发考勤组" --timeout 10
source: internal/helpers/attendance.go:2669
visible_flags: 8

## Flags
- --group-id <Int64>: 考勤组 ID（必填）
- --name <String>: 考勤组名称（可选）
- --type <String>: 考勤组类型：FIXED 固定班制 / TURN 排班制 / NONE 自由工时（可选）
- --owner <String>: 考勤组主负责人 userId（可选）
- --enable-outside-check <String>: 是否允许外勤打卡，传 true 或 false（可选）
- --classIds <String>: 所选班次 id 列表，JSON 数组格式，如 '[123,456]'（可选）
- --group-vo <String>: 完整 groupVO JSON 字符串，用于修改复杂子对象（可选）
- --yes <Bool>: 跳过确认提示

## Related
- dws attendance group create
- dws attendance group filtered-get
- dws attendance group get
- dws attendance group search
- dws attendance group update-members
