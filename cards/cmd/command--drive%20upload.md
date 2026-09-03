# dws drive upload

kind: command
completeness: full
usage: dws drive upload
description: 上传本地文件到钉盘或文档空间
example: dws drive upload --file ./report.pdf
source: internal/helpers/drive.go:1467
visible_flags: 8

## Flags
- --file <String>: 本地文件路径 (必填)
- --file-name <String>: 文件显示名称 (默认使用文件名)
- --space-id <String>: 目标钉盘空间 ID，不传则使用「我的文件」 (可选)
- --mime-type <String>: 文件 MIME 类型，不传则自动推断 (可选)
- --folder <String>: 父节点 ID，不传则上传到空间根目录 (可选，与 --node 互斥)
- --workspace <String>: 目标知识库 ID，传入时路由到文档空间上传 (可选)
- --convert <Bool>: 是否转换为钉钉在线文档 (仅文档空间上传时生效)
- --node <String>: 覆盖目标文件 ID，传入即覆盖已有文件（与 --folder 互斥）(可选)

## Related
- dws drive comment
- dws drive commit
- dws drive copy
- dws drive cover
- dws drive delete
- dws drive download
