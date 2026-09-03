# dws doc media upload

kind: command
completeness: full
usage: dws doc media upload
description: 上传可复用的文档媒体资源
example: dws doc media upload --node DOC_ID --file ./icon.svg --mime-type image/svg+xml --format json
source: internal/helpers/doc.go:2943
visible_flags: 5

## Flags
- --node <String>: 绑定媒体资源的文档标识，支持传入 URL 或 ID (必填)
- --file <String>: 本地文件路径 (必填)
- --name <String>: 资源文件名 (默认使用本地文件名)
- --mime-type <String>: 文件 MIME 类型 (默认根据扩展名推断)
- --yes <Bool>: 确认上传可复用文档媒体资源

## Related
- dws doc media download
- dws doc media insert
