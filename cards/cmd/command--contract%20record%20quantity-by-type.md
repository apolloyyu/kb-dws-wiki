# dws contract record quantity-by-type

kind: command
completeness: full
usage: dws contract record quantity-by-type
description: 按查询维度统计各状态合同数量
example: dws contract record quantity-by-type --format json
source: internal/helpers/contract.go:144
visible_flags: 1

## Flags
- --type <String>: 查询维度: self|participation|department|all|unassigned（默认 all，与 MCP queryContractQuantityByType 的 type 一致）

## Related
- dws contract record create
- dws contract record get
- dws contract record list
