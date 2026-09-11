# dws whiteboard query

kind: command
completeness: full
usage: dws whiteboard query
description: 读取白板内容
example: dws whiteboard query --node DOC_ID_OR_URL --part-id WHITEBOARD_PART_ID --format json
source: internal/helpers/whiteboard.go:71
visible_flags: 4

## Flags
- --node <String>: 承载文档或独立白板的节点 ID/URL（必填）
- --part-id <String>: 文档内白板 part ID；显式提供时选择内嵌白板
- --view <String>: 独立白板查询视图: summary / page / all
- --page-id <String>: 独立白板页面 ID（view=page 时必填）

## Related
- dws whiteboard create-with-content
- dws whiteboard export
- dws whiteboard export-get
- dws whiteboard update
