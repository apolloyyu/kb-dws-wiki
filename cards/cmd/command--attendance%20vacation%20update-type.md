# dws attendance vacation update-type

kind: command
completeness: full
usage: dws attendance vacation update-type
description: 更新假期规则
example: dws attendance vacation update-type --leave-code a1b2c3d4-e5f6-7890-abcd-ef1234567890 --name "事假（修改版）"
source: internal/helpers/attendance.go:3871
visible_flags: 8

## Flags
- --leave-code <String>: 假期编码（必填）
- --name <String>: 假期名称（可选）
- --unit <String>: 假期单位：day/halfDay/hour（可选）
- --paid <Bool>: 是否带薪假期（可选）
- --per-hours <Int>: 一天折算小时数（可选）
- --when-can-leave <String>: 新员工请假规则：entry/formal（可选）
- --visibility-rules <String>: 适用范围规则 JSON 数组（可选）。不传=不改；[{\"type\":\"dept\",\"visible\":[\"-1\"]}]=全公司可见（哨兵）；其余=改为指定范围。空数组/无效规则会报错
- --user-say-yes <Bool>: 用户已确认，跳过交互式确认提示（Agent 调用时传 true 前必须完成用户二次确认）

## Related
- dws attendance vacation balance
- dws attendance vacation records
- dws attendance vacation save-balance
- dws attendance vacation types
