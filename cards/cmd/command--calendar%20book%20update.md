# dws calendar book update

kind: command
completeness: full
usage: dws calendar book update
description: 更新指定日历本
example: dws calendar book update --id CALENDAR_ID --summary "新日历名"
source: internal/helpers/calendar.go:1593
visible_flags: 3

## Flags
- --id <String>: 日历 ID (必填)
- --summary <String>: 日历标题
- --desc <String>: 日历描述

## Related
- dws calendar book get
- dws calendar book list
- dws calendar book search
