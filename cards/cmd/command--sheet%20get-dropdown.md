# dws sheet get-dropdown

kind: command
completeness: full
usage: dws sheet get-dropdown
description: 获取下拉列表配置
example: dws sheet get-dropdown --node NODE_ID --sheet-id SHEET_ID --range "A2:A100"
source: internal/helpers/sheet_dimension.go:939
visible_flags: 3

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称 (必填)
- --range <String>: 查询范围，A1 表示法，如 A1:A100 (必填)

## Related
- dws sheet add-dimension
- dws sheet append
- dws sheet batch-update
- dws sheet changeset-get
- dws sheet chart
- dws sheet comment
