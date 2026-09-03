# dws sheet copy

kind: command
completeness: full
usage: dws sheet copy
description: 复制工作表
example: dws sheet copy --node NODE_ID --sheet-id SHEET_ID
source: internal/helpers/sheet_workbook.go:372
visible_flags: 5

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 源工作表 ID 或名称 (必填)
- --name <String>: 副本名称，最长 100 字符 (不传则系统自动生成)
- --title <String>: --name 的别名（兼容）
- --index <Int>: 副本位置索引，0-based (不传则放在源工作表之后)

## Related
- dws sheet add-dimension
- dws sheet append
- dws sheet batch-update
- dws sheet changeset-get
- dws sheet chart
- dws sheet comment
