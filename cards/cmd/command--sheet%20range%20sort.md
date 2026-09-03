# dws sheet range sort

kind: command
completeness: full
usage: dws sheet range sort
description: 对工作表指定区域排序
example: dws sheet range sort --node NODE_ID --sheet-id SHEET_ID --range "A1:D10"
source: internal/helpers/sheet_range_ops.go:364
visible_flags: 5

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称 (必填)
- --range <String>: 排序范围，A1 表示法 (必填，如 A1:D10)
- --sort-keys <String>: ascending
- --has-header <Bool>: 首行是否为表头（不参与排序）

## Related
- dws sheet range batch-clear
- dws sheet range batch-set-style
- dws sheet range clear
- dws sheet range copy-to
- dws sheet range fill
- dws sheet range move-to
