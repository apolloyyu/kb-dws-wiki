# dws whiteboard create-with-content

kind: command
completeness: partial
usage: dws whiteboard create-with-content
description: —
source: internal/helpers/whiteboard_standalone.go:23
visible_flags: 6
partial_reason: missing_description

## Flags
- --name <String> required: 独立白板名称（必填）
- --source <String> required: OpenNodes V1 JSON String 或 JSON 文件路径（必填）
- --request-id <String> required: 1-128 字符稳定幂等请求 ID（必填）
- --expected-source-digest <String>: 可选的 render sourceDigest；确保提交内容与已确认预览一致
- --folder <String>: 目标文件夹节点 ID/URL
- --workspace <String>: 目标知识库 ID/URL

## Related
- dws whiteboard export
- dws whiteboard export-get
- dws whiteboard query
- dws whiteboard render
- dws whiteboard template
- dws whiteboard update
