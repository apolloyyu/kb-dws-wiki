# dws doc +media-preview

kind: shortcut
completeness: full
description: 下载正文媒体到受控临时目录并返回预览路径
source: internal/shortcut/doc/media_style_shortcuts.go:91
visible_flags: 2

## Flags
- --node <String>: 文档 ID 或 URL
- --resource-id <String>: 附件 resourceId；--resource-id 必须是附件回执返回的 UUID

## Related
- dws doc +background-delete
- dws doc +background-update
- dws doc +checkpoint-update
- dws doc +comment-create
- dws doc +comment-create-inline
- dws doc +comment-delete
