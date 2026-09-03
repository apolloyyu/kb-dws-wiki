# dws attendance class create

kind: command
completeness: full
usage: dws attendance class create
description: 创建班次
example: dws attendance class create --name "早班" --class-vo '{"sections":[{"times":[{"checkType":"OnDuty","checkTime":"08:00","across":0},{"checkType":"OffDuty","checkTime":"17:00","across":0}]}]}' --timeout 10
source: internal/helpers/attendance.go:1642
visible_flags: 4

## Flags
- --name <String>: 班次名称（必填）
- --owner <String>: 班次负责人 userId（可选）
- --class-vo <String>: 完整 TopAtClassVO JSON 字符串，包含 sections 等复杂子对象（必填）
- --yes <Bool>: 跳过确认提示

## Related
- dws attendance class get
- dws attendance class search
- dws attendance class update
