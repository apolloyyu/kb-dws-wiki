# dws calendar book get

kind: command
completeness: full
usage: dws calendar book get
description: 查询指定日历本
example: dws calendar book get --id primary
source: internal/helpers/calendar.go:1491
visible_flags: 1

## Flags
- --id <String>: 日历 ID (必填，主日历固定为 primary)

## Related
- dws calendar book list
- dws calendar book search
- dws calendar book update
