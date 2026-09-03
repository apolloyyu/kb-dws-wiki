# dws sheet range batch-set-style

kind: command
completeness: partial
usage: dws sheet range batch-set-style
description: 批量设置样式（服务端原子事务）
example: dws sheet range batch-set-style --node NODE_ID
source: internal/helpers/sheet_style.go:594
visible_flags: 22
partial_reason: unverified_flags,too_many_flags:22

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --ranges <String>: Sheet2!D1:D10
- --batch <String>: 批次配置 JSON 文件路径（与 --ranges 二选一，每项可用不同样式）
- --continue-on-error <Bool>: 遇到失败时继续执行其余项（默认严格事务，整批回滚）
- --bg-color <String>: 背景色（#RRGGBB），一键刷满目标区域；与 --bg-colors-json 二选一
- --bg-colors-json <String>: 背景色二维 JSON 数组，维度需与目标区域一致
- --font-size <Int>: 字号，一键刷满目标区域；与 --font-sizes-json 二选一
- --font-sizes-json <String>: 字号二维 JSON 数组，维度需与目标区域一致
- … 14 more; use dwsdoc cmd/short for full flags

## Related
- dws sheet range batch-clear
- dws sheet range clear
- dws sheet range copy-to
- dws sheet range fill
- dws sheet range move-to
- dws sheet range read
