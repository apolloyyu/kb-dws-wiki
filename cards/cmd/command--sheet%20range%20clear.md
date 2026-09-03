# dws sheet range clear

kind: command
completeness: full
description: 清除工作表指定区域
source: internal/helpers/sheet_range_ops.go:295
visible_flags: 4

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称 (必填)
- --range <String>: 清除范围，A1 表示法 (必填，如 A1:B3)
- --type <String>: 清除类型: content(仅值,默认) / format(仅格式) / all(全部)

## Related
- dws sheet range batch-clear
- dws sheet range batch-set-style
- dws sheet range copy-to
- dws sheet range fill
- dws sheet range move-to
- dws sheet range read
