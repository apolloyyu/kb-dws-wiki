# dws sheet range set-style

kind: command
completeness: partial
usage: dws sheet range set-style
description: 设置指定单元格区域的样式
example: dws sheet range set-style --node NODE_ID --sheet-id SHEET_ID --range "A1:B3"
source: internal/helpers/sheet_style.go:488
visible_flags: 21
partial_reason: unverified_flags,too_many_flags:21

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称 (必填)
- --range <String>: 目标单元格区域地址，如 A1:B3 (必填)
- --bg-color <String>: 背景色（#RRGGBB），一键刷满目标区域；与 --bg-colors-json 二选一
- --bg-colors-json <String>: 背景色二维 JSON 数组，维度需与目标区域一致
- --font-size <Int>: 字号，一键刷满目标区域；与 --font-sizes-json 二选一
- --font-sizes-json <String>: 字号二维 JSON 数组，维度需与目标区域一致
- --h-align <String>: 水平对齐（left/center/right/general），一键刷满目标区域
- … 13 more; use dwsdoc cmd/short for full flags

## Related
- dws sheet range batch-clear
- dws sheet range batch-set-style
- dws sheet range clear
- dws sheet range copy-to
- dws sheet range fill
- dws sheet range move-to
