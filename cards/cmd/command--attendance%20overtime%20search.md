# dws attendance overtime search

kind: command
completeness: full
usage: dws attendance overtime search
description: 查询当前用户可管理的加班规则列表
example: dws attendance overtime search --page 1 --limit 20
source: internal/helpers/attendance.go:2042
visible_flags: 3

## Flags
- --query <String>: 加班规则名称关键字，模糊搜索（可选）
- --page <Int>: 页码，从 1 开始（默认 1，可选）
- --limit <Int>: 每页条数，200 以内（默认 20，可选）

## Related
- dws attendance overtime get
