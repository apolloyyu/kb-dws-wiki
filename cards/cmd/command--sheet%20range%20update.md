# dws sheet range update

kind: command
completeness: full
usage: dws sheet range update
description: 更新工作表指定区域内容
example: dws sheet range update --node NODE_ID --sheet-id SHEET_ID --range "A1:B2"
source: internal/helpers/sheet_range_ops.go:119
visible_flags: 4

## Flags
- --node <String>: 表格文档 ID (必填)
- --sheet-id <String>: 工作表 ID 或名称 (必填)
- --range <String>: 目标单元格区域地址，如 A1:B3 (必填)
- --values <String>: 单元格内容，二维 JSON 数组 (必填)；每个元素必须是 object：{type:text,text:...}、{type:richText,texts:[...]}、{dataValidation:...}、{cellStyles:...}、{hyperlink:...} 或 {}（详见 --help 长描述）

## Related
- dws sheet range batch-clear
- dws sheet range batch-set-style
- dws sheet range clear
- dws sheet range copy-to
- dws sheet range fill
- dws sheet range move-to
