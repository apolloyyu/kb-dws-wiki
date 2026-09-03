# dws sheet create-with-data

kind: command
completeness: partial
usage: dws sheet create-with-data
description: 创建钉钉表格文档并写入初始数据（可选样式）
example: dws sheet create-with-data --name "名单" --values '[["姓名","分数"],["张三","90"]]'
source: internal/helpers/sheet_create_with_data.go:40
visible_flags: 6
partial_reason: unverified_flags

## Flags
- --name <String>: 表格名称 (必填)
- --folder <String>: 目标文件夹 ID 或 URL
- --workspace <String>: 目标知识库 ID
- --values <String>: 初始数据，二维 JSON 数组，写入默认工作表 (与 --sheets 二选一)
- --sheets <String>: data
- --styles <String>: all

## Related
- dws sheet add-dimension
- dws sheet append
- dws sheet batch-update
- dws sheet changeset-get
- dws sheet chart
- dws sheet comment
