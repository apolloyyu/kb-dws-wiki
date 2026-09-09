# dws contract account update

kind: command
completeness: full
usage: dws contract account update
description: 更新账款信息
example: dws contract account update --file ./account_update.json --format json
source: internal/helpers/contract.go:552
visible_flags: 1

## Flags
- --file <String>: UpdateContractAccountRequest JSON 文件路径，\"-\" 表示 stdin（必填）

## Related
- dws contract account create
- dws contract account delete
- dws contract account get
- dws contract account list
