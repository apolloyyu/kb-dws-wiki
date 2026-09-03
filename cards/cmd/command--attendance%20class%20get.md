# dws attendance class get

kind: command
completeness: full
usage: dws attendance class get
description: 根据班次 ID 查询班次详情
example: dws attendance class get --class-id 1170996821
source: internal/helpers/attendance.go:1591
visible_flags: 1

## Flags
- --class-id <Int64>: 班次 ID（必填）

## Related
- dws attendance class create
- dws attendance class search
- dws attendance class update
