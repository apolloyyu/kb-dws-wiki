# dws contract account delete

kind: command
completeness: full
usage: dws contract account delete
description: 删除账款信息
example: dws contract account delete --account-id 12345 --format json
source: internal/helpers/contract.go:680
visible_flags: 1

## Flags
- --account-id <Int64>: 账款 ID（必填）

## Related
- dws contract account create
- dws contract account get
- dws contract account list
- dws contract account update
