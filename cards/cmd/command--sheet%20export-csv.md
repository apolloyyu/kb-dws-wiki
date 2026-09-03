# dws sheet export-csv

kind: command
completeness: full
description: 导出单个工作表为纯 CSV（同步）
source: internal/helpers/sheet_export_csv.go:29
visible_flags: 6

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称（不传则第一个工作表）
- --range <String>: 导出范围，A1 表示法（不传则整表；大表可用此分块导出）
- --value-render-option <String>: 取值模式: formatted_value(默认) / raw_value / formula
- --output <String>: 本地保存路径（可选，支持文件路径或目录）；不传则输出到 stdout
- --allow-truncated <Bool>: 允许数据被截断时仍然导出。默认截断即报错并不写文件，避免不完整数据被当成完整导出

## Related
- dws sheet add-dimension
- dws sheet append
- dws sheet batch-set-style
- dws sheet batch-update
- dws sheet changeset-get
- dws sheet comment
