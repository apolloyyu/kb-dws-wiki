# dws sheet range batch-clear

kind: command
completeness: partial
usage: dws sheet range batch-clear
description: 批量清除多个区域（原子事务）
example: dws sheet range batch-clear --node NODE_ID --ranges '["Sheet1!A1:B3","Sheet2!C1:D5"]'
source: internal/helpers/sheet_batch.go:1602
visible_flags: 0
partial_reason: unverified_flags

## Flags
- none

## Related
- dws sheet range batch-set-style
- dws sheet range clear
- dws sheet range copy-to
- dws sheet range fill
- dws sheet range move-to
- dws sheet range read
