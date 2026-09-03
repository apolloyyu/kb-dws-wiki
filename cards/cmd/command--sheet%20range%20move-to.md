# dws sheet range move-to

kind: command
completeness: full
usage: dws sheet range move-to
description: 移动工作表指定区域到目标位置
example: dws sheet range move-to --node NODE_ID --sheet-id SHEET_ID
source: internal/helpers/sheet_range_ops.go:585
visible_flags: 5

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 源工作表 ID 或名称 (必填)
- --source-range <String>: 源范围，A1 表示法 (必填，如 A1:C5)
- --target-range <String>: 目标位置，A1 表示法 (必填，如 D1；支持 Sheet2!A1 表示法指定目标工作表)
- --target-sheet-id <String>: 目标工作表 ID 或名称（可选，不传则移动到同一工作表）

## Related
- dws sheet range batch-clear
- dws sheet range batch-set-style
- dws sheet range clear
- dws sheet range copy-to
- dws sheet range fill
- dws sheet range read
