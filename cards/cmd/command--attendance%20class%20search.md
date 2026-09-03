# dws attendance class search

kind: command
completeness: full
usage: dws attendance class search
description: 查询当前用户可管理的所有班次详情
example: dws attendance class search
source: internal/helpers/attendance.go:1518
visible_flags: 4

## Flags
- --page <Int>: 页码，从 1 开始（可选）
- --limit <Int>: 每页条数，最大 200（可选）
- --query <String>: 班次名称关键字，模糊搜索（可选）
- --filter-type <String>: 班次类型：ALL 全部班次 / MINE_OWN 我负责的（可选）

## Related
- dws attendance class create
- dws attendance class get
- dws attendance class update
