# dws contract account get

kind: command
completeness: full
usage: dws contract account get
description: 获取账款信息
example: dws contract account get --account-id 12345 --format json
source: internal/helpers/contract.go:585
visible_flags: 1

## Flags
- --account-id <Int64>: 账款 ID（必填）

## Related
- dws contract account create
- dws contract account delete
- dws contract account list
- dws contract account update
