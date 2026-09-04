# dws contract record list

kind: command
completeness: full
usage: dws contract record list
description: 查询合同列表
example: dws contract record list --format json
source: internal/helpers/contract.go:79
visible_flags: 4

## Flags
- --start <String>: 合同创建时间范围起点（ISO-8601，如 2026-03-10T14:00:00+08:00）
- --end <String>: 合同创建时间范围终点（ISO-8601，须晚于 --start）
- --status <String>: 合同状态，英文枚举，逗号分隔
- --type <String>: 查询维度: self|participation|department|all|unassigned（默认 all，与 MCP queryContracts 的 type 一致）

## Related
- dws contract record create
- dws contract record get
- dws contract record quantity-by-type
