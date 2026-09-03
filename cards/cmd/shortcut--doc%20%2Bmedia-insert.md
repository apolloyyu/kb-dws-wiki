# dws doc +media-insert

kind: shortcut
completeness: full
usage: dws doc +media-insert
description: 上传本地图片或文件并插入文档正文
source: internal/shortcut/doc/media_style_shortcuts.go:39
visible_flags: 7

## Flags
- --node <String>: 文档 ID 或 URL
- --file <String>: 工作目录内已存在的相对文件路径
- --name <String>: 显示名称
- --mime-type <String>: MIME 类型
- --index <Int>: 顶层插入索引
- --where <String>: 相对参考块的位置
- --ref-block <String>: 参考 block ID

## Related
- dws doc +background-delete
- dws doc +background-update
- dws doc +checkpoint-update
- dws doc +comment-create
- dws doc +comment-create-inline
- dws doc +comment-delete
