# dws whiteboard export-get

kind: command
completeness: full
usage: dws whiteboard export-get
description: 查询白板导出任务并下载
source: internal/helpers/whiteboard_export.go:51
visible_flags: 3

## Flags
- --job-id <String>: 导出任务 ID（必填）
- --export-format <String>: 导出格式: png / pdf
- --output <String>: 本地目标目录（必填）

## Related
- dws whiteboard create-with-content
- dws whiteboard export
- dws whiteboard query
- dws whiteboard update
