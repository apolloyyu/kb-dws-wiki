# dws sheet info

kind: command
completeness: full
usage: dws sheet info
description: 获取指定工作表详情
example: dws sheet info --node NODE_ID
source: internal/helpers/sheet_workbook.go:122
visible_flags: 3

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称 (不传则返回第一个工作表)
- --include <StringSlice>: 可选扩展信息，逗号分隔；支持 groups / row_heights / col_widths / hidden_rows / hidden_cols / frozen

## Related
- dws sheet add-dimension
- dws sheet append
- dws sheet batch-update
- dws sheet changeset-get
- dws sheet chart
- dws sheet comment
