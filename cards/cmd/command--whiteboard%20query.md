# dws whiteboard query

kind: command
completeness: full
usage: dws whiteboard query
description: 读取白板内容
example: dws whiteboard query --node DOC_ID_OR_URL --part-id WHITEBOARD_PART_ID --format json
source: internal/helpers/whiteboard.go:64
visible_flags: 2

## Flags
- --node <String>: 承载白板的钉钉文档 ID 或 URL（必填）
- --part-id <String>: 文档内白板 part ID（必填）

## Related
- dws whiteboard update
