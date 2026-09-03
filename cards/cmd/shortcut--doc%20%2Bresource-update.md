# dws doc +resource-update

kind: shortcut
completeness: full
usage: dws doc +resource-update
description: 从本地图片或 HTTPS URL 设置文档封面
source: internal/shortcut/doc/media_style_shortcuts.go:132
visible_flags: 3

## Flags
- --node <String>: 文档 ID 或 URL
- --image <String>: HTTPS 封面图片 URL
- --file <String>: 工作目录内已存在封面图片的相对路径

## Related
- dws doc +background-delete
- dws doc +background-update
- dws doc +checkpoint-update
- dws doc +comment-create
- dws doc +comment-create-inline
- dws doc +comment-delete
