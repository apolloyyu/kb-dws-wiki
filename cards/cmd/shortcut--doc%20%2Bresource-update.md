# dws doc +resource-update

kind: shortcut
completeness: full
usage: dws doc +resource-update
description: 从本地图片或 HTTPS URL 设置文档封面
source: internal/shortcut/doc/media_style_shortcuts.go:148
visible_flags: 5

## Flags
- --from-clipboard <Bool>: 读取系统剪贴板PNG，与本地file及image互斥
- --position <String>: —
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
