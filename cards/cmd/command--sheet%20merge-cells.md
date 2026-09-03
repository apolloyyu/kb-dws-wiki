# dws sheet merge-cells

kind: command
completeness: full
usage: dws sheet merge-cells
description: 合并单元格
example: dws sheet merge-cells --node NODE_ID --sheet-id SHEET_ID --range "A1:B3"
source: internal/helpers/sheet_dimension.go:299
visible_flags: 4

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称 (必填)
- --range <String>: 目标单元格区域地址，如 A1:B3 (必填)
- --merge-type <String>: 合并方式: mergeAll(默认)/mergeRows/mergeColumns

## Related
- dws sheet add-dimension
- dws sheet append
- dws sheet batch-update
- dws sheet changeset-get
- dws sheet chart
- dws sheet comment
