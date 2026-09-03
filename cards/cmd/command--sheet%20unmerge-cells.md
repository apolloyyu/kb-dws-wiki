# dws sheet unmerge-cells

kind: command
completeness: full
description: 取消合并单元格
source: internal/helpers/sheet_dimension.go:376
visible_flags: 3

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称 (必填)
- --range <String>: 取消合并的范围，A1 表示法，如 A1:D5 (必填)

## Related
- dws sheet add-dimension
- dws sheet append
- dws sheet batch-set-style
- dws sheet batch-update
- dws sheet changeset-get
- dws sheet comment
