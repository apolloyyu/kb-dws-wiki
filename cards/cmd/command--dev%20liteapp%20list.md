# dws dev liteapp list

kind: command
completeness: partial
usage: dws dev liteapp list
description: —
source: internal/helpers/dev_liteapp.go:261
visible_flags: 2
partial_reason: missing_description

## Flags
- --size <Int>: 每页数量，默认 20，上限 50
- --offset <Int>: 偏移量，从 0 开始

## Related
- dws dev liteapp create
- dws dev liteapp credential
- dws dev liteapp delete
- dws dev liteapp detail
- dws dev liteapp update
