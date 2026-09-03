# dws attendance group create

kind: command
completeness: full
usage: dws attendance group create
description: 创建考勤组
example: dws attendance group create --name "研发考勤组" --type FIXED --group-vo '{"defaultClassId":1170996821,"workDayClassList":[0,1170996821,0,0,0,0,0]}' --timeout 10
source: internal/helpers/attendance.go:2417
visible_flags: 6

## Flags
- --name <String>: 考勤组名称（必填）
- --type <String>: 考勤组类型：FIXED（固定班制）/ TURN（排班制）/ NONE（自由工时）（必填）
- --owner <String>: 考勤组主负责人 userId（可选）
- --corp-id <String>: 企业 corpId（可选，不传时由登录上下文自动补齐）
- --group-vo <String>: 完整 groupVO JSON 字符串（可选，用于传入复杂子对象，会与 --name/--type/--owner 合并）
- --yes <Bool>: 跳过确认提示

## Related
- dws attendance group filtered-get
- dws attendance group get
- dws attendance group search
- dws attendance group update
- dws attendance group update-members
