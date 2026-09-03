# dws sheet import

kind: command
completeness: full
usage: dws sheet import
description: 导入本地表格文件为在线电子表格 (xlsx / xls)
example: dws sheet import --file ./quote.xlsx --folder-token <FOLDER_TOKEN>
source: internal/helpers/sheet_import.go:44
visible_flags: 4

## Flags
- --file <String>: 本地表格文件路径 (必填，支持 xlsx/xls)
- --folder-token <String>: 目标文件夹 ID 或 URL (与 --workspace 至少传一个)
- --workspace <String>: 目标知识库 ID 或 URL (与 --folder-token 至少传一个)
- --name (-n) <String>: 导入后表格名称 (可选，默认取文件名)

## Related
- dws sheet add-dimension
- dws sheet append
- dws sheet batch-update
- dws sheet changeset-get
- dws sheet chart
- dws sheet comment
