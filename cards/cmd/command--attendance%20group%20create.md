# dws attendance group create

kind: command
completeness: full
description: 创建班次
source: internal/helpers/attendance.go:1642
visible_flags: 4

## Flags
- --name <String>: 班次名称（必填）
- --owner <String>: 班次负责人 userId（可选）
- --class-vo <String>: 完整 TopAtClassVO JSON 字符串，包含 sections 等复杂子对象（必填）
- --yes <Bool>: 跳过确认提示

## Related
- dws attendance group filtered-get
- dws attendance group get
- dws attendance group search
- dws attendance group update
- dws attendance group update-members
