# dws doc +inspect

kind: shortcut
completeness: full
description: 聚合文档元信息，并按需附带样式、权限、历史、媒体和评论
source: internal/shortcut/doc/content_shortcuts.go:302
visible_flags: 6

## Flags
- --node <String>: 文档 ID 或 URL
- --include-style <Bool>: 附带封面和背景
- --include-permissions <Bool>: 附带权限列表
- --include-history <Bool>: 附带最近历史版本
- --include-media <Bool>: 附带正文媒体列表
- --include-comments <Bool>: 附带评论列表

## Related
- dws doc +background-delete
- dws doc +background-update
- dws doc +checkpoint-update
- dws doc +comment-create
- dws doc +comment-create-inline
- dws doc +comment-delete
