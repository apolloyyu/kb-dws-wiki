# dws contract account create

kind: command
completeness: full
usage: dws contract account create
description: 创建账款信息
example: dws contract account create --file ./account.json --format json
source: internal/helpers/contract.go:520
visible_flags: 1

## Flags
- --file <String>: CreateContractAccountRequest JSON 文件路径，\"-\" 表示 stdin（必填）

## Related
- dws contract account delete
- dws contract account get
- dws contract account list
- dws contract account update
