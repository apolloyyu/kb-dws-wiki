# dws attendance class update

kind: command
completeness: full
usage: dws attendance class update
description: 更新班次
example: dws attendance class update --class-id 1170996821 --name "新早班" --timeout 10
source: internal/helpers/attendance.go:1749
visible_flags: 5

## Flags
- --class-id <Int64>: 班次 ID（必填）
- --name <String>: 班次名称（可选，不传则保持原值）
- --owner <String>: 班次负责人 userId（可选，不传则保持原值）
- --class-vo <String>: 完整 TopAtClassVO JSON 字符串，包含 sections 等复杂子对象（可选）
- --yes <Bool>: 跳过确认提示

## Related
- dws attendance class create
- dws attendance class get
- dws attendance class search
