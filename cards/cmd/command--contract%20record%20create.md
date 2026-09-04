# dws contract record create

kind: command
completeness: full
usage: dws contract record create
description: 创建合同台账
example: dws contract record create --file ./contract.json --format json
source: internal/helpers/contract.go:165
visible_flags: 1

## Flags
- --file <String>: ImportContractInfoRequest JSON 文件路径，\"-\" 表示 stdin（必填）

## Related
- dws contract record get
- dws contract record list
- dws contract record quantity-by-type
