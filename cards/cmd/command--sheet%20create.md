# dws sheet create

kind: command
completeness: full
usage: dws sheet create
description: 创建钉钉表格文档
example: dws sheet create --name "销售数据"
source: internal/helpers/sheet_workbook.go:11
visible_flags: 3

## Flags
- --name <String>: 表格名称 (必填)
- --folder <String>: 目标文件夹 ID 或 URL
- --workspace <String>: 目标知识库 ID

## Related
- dws sheet add-dimension
- dws sheet append
- dws sheet batch-update
- dws sheet changeset-get
- dws sheet chart
- dws sheet comment
