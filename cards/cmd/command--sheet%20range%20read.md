# dws sheet range read

kind: command
completeness: full
description: 读取工作表数据（别名: get）
source: internal/helpers/sheet_range_ops.go:17
visible_flags: 4

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称 (不传则默认第一个工作表)
- --range <String>: 读取范围，A1 表示法 (如 A1:D10，不传则读取全部数据)
- --value-render-option <String>: 取值模式: formatted_value(默认) | raw_value | formula

## Related
- dws sheet range batch-clear
- dws sheet range batch-set-style
- dws sheet range clear
- dws sheet range copy-to
- dws sheet range fill
- dws sheet range move-to
