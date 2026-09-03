# dws calendar book search

kind: command
completeness: full
usage: dws calendar book search
description: 搜索日历本
example: dws calendar book search --query "项目"
source: internal/helpers/calendar.go:1542
visible_flags: 1

## Flags
- --query <String>: 按日历本名称模糊检索 (必填)

## Related
- dws calendar book get
- dws calendar book list
- dws calendar book update
