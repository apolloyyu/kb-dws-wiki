# dws whiteboard update

kind: command
completeness: full
description: 追加或整页重建白板内容
source: internal/helpers/whiteboard.go:115
visible_flags: 4

## Flags
- --node <String>: 承载白板的钉钉文档 ID 或 URL（必填）
- --part-id <String>: 文档内白板 part ID（必填）
- --source <String>: OpenNodes V1 更新请求 JSON 文件（必填）
- --yes <Bool>: 确认写入远端白板

## Related
- dws whiteboard query
