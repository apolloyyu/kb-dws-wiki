# dws sheet range copy-to

kind: command
completeness: full
description: 复制工作表指定区域到目标位置
source: internal/helpers/sheet_range_ops.go:511
visible_flags: 6

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 源工作表 ID 或名称 (必填)
- --source-range <String>: 源范围，A1 表示法 (必填，如 A1:C5)
- --target-range <String>: 目标位置，A1 表示法 (必填，如 D1；支持 Sheet2!A1 表示法指定目标工作表)
- --target-sheet-id <String>: 目标工作表 ID 或名称（可选，不传则复制到同一工作表）
- --paste-type <String>: 粘贴类型: values(仅值) / formulas(仅公式) / formats(仅格式) / all(全部,默认)

## Related
- dws sheet range batch-clear
- dws sheet range batch-set-style
- dws sheet range clear
- dws sheet range fill
- dws sheet range move-to
- dws sheet range read
