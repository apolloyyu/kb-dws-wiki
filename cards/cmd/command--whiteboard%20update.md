# dws whiteboard update

kind: command
completeness: full
usage: dws whiteboard update
description: 追加或整页重建白板内容
example: dws whiteboard update --node DOC_ID_OR_URL --part-id WHITEBOARD_PART_ID --source ./whiteboard.json --format json
source: internal/helpers/whiteboard.go:115
visible_flags: 4

## Flags
- --node <String>: 承载白板的钉钉文档 ID 或 URL（必填）
- --part-id <String>: 文档内白板 part ID（必填）
- --source <String>: OpenNodes V1 更新请求 JSON 文件（必填）
- --yes <Bool>: 确认写入远端白板

## Related
- dws whiteboard query
