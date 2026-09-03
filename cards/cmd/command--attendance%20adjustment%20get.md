# dws attendance adjustment get

kind: command
completeness: full
usage: dws attendance adjustment get
description: 根据补卡规则主键 ID 查询补卡规则详情
example: dws attendance adjustment get --adjustment-id 12345
source: internal/helpers/attendance.go:1865
visible_flags: 1

## Flags
- --adjustment-id <Int64>: 补卡规则主键 ID（必填）

## Related
- dws attendance adjustment search
