# dws attendance overtime get

kind: command
completeness: full
usage: dws attendance overtime get
description: 根据加班规则主键 ID 查询加班规则详情
example: dws attendance overtime get --overtime-id 12345
source: internal/helpers/attendance.go:1990
visible_flags: 1

## Flags
- --overtime-id <Int64>: 加班规则主键 ID（必填）

## Related
- dws attendance overtime search
