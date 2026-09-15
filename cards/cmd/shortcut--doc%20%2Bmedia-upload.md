# dws doc +media-upload

kind: shortcut
completeness: full
usage: dws doc +media-upload
description: 上传同文档可复用媒体并下载校验字节，不插入正文
source: internal/shortcut/doc/media_upload_shortcut.go:23
visible_flags: 4

## Flags
- --node <String>: —
- --file <String>: —
- --name <String>: 可选资源文件名
- --mime-type <String>: 可选MIME类型，默认按扩展名

## Related
- dws doc +background-delete
- dws doc +background-update
- dws doc +checkpoint-update
- dws doc +comment-create
- dws doc +comment-create-inline
- dws doc +comment-delete
