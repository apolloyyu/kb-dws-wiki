# dws sheet range set-style

kind: command
completeness: full
description: 设置指定单元格区域的样式
source: internal/helpers/sheet_style.go:488
visible_flags: 3

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称 (必填)
- --range <String>: 目标单元格区域地址，如 A1:B3 (必填)

## Related
- dws sheet range batch-clear
- dws sheet range batch-set-style
- dws sheet range clear
- dws sheet range copy-to
- dws sheet range fill
- dws sheet range move-to
