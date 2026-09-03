# dws sheet range fill

kind: command
completeness: full
description: 自动填充工作表指定区域
source: internal/helpers/sheet_range_ops.go:442
visible_flags: 5

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称 (必填)
- --source-range <String>: 源数据范围，A1 表示法 (必填，如 A1:A5)
- --target-range <String>: 目标填充范围，A1 表示法 (必填，如 A6:A20)
- --fill-type <String>: 填充类型: 不传则自动检测 / copy(复制) / onlystyle(仅格式) / withoutstyle(仅值)

## Related
- dws sheet range batch-clear
- dws sheet range batch-set-style
- dws sheet range clear
- dws sheet range copy-to
- dws sheet range move-to
- dws sheet range read
