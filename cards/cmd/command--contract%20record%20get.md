# dws contract record get

kind: command
completeness: full
usage: dws contract record get
description: 查询合同详情
example: dws contract record get --contract-id "c_xxx" --format json
source: internal/helpers/contract.go:125
visible_flags: 1

## Flags
- --contract-id <String>: 合同 ID（必填，对应 MCP queryContractDetails 的 contractId）

## Related
- dws contract record create
- dws contract record list
- dws contract record quantity-by-type
