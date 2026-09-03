# dws sheet export

kind: command
completeness: full
description: 导出表格为 xlsx（异步任务一站式）
source: internal/helpers/sheet_export.go:247
visible_flags: 2

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --output <String>: 本地保存路径（可选，支持文件路径或目录）

## Related
- dws sheet add-dimension
- dws sheet append
- dws sheet batch-set-style
- dws sheet batch-update
- dws sheet changeset-get
- dws sheet comment
