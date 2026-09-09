# dws whiteboard export

kind: command
completeness: full
usage: dws whiteboard export
description: 导出独立白板到本地
example: dws whiteboard export --node <WHITEBOARD_NODE_ID> --output ./exports --format json
source: internal/helpers/whiteboard_export.go:39
visible_flags: 3

## Flags
- --node <String>: 独立白板节点 ID/URL（必填）
- --export-format <String>: 导出格式: png / pdf
- --output <String>: 本地目标目录（必填，文件名自动使用白板名称）

## Related
- dws whiteboard create-with-content
- dws whiteboard export-get
- dws whiteboard query
- dws whiteboard update
