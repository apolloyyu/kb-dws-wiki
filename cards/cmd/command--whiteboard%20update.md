# dws whiteboard update

kind: command
completeness: full
usage: dws whiteboard update
description: 追加或整页重建白板内容
example: dws whiteboard update --node DOC_ID_OR_URL --part-id WHITEBOARD_PART_ID --source ./whiteboard.json --format json
source: internal/helpers/whiteboard.go:142
visible_flags: 7

## Flags
- --node <String>: 承载文档或独立白板的节点 ID/URL（必填）
- --part-id <String>: 文档内白板 part ID；显式提供时选择内嵌白板
- --source <String>: OpenNodes V1 更新请求 JSON 文件（必填）
- --page-id <String>: 目标页面 ID；独立白板 overwrite 时必填
- --expected-revision <Int>: 独立白板最新 revision（独立分支必填）
- --request-id <String>: 独立白板稳定幂等请求 ID（独立分支必填）
- --yes <Bool>: 确认写入远端白板

## Related
- dws whiteboard create-with-content
- dws whiteboard export
- dws whiteboard export-get
- dws whiteboard query
