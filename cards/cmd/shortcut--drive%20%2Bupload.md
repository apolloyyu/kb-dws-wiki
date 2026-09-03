# dws drive +upload

kind: shortcut
completeness: full
description: 从工作目录上传普通文件到钉盘或文档空间并读回验证
source: internal/shortcut/drive/catalog_operations.go:430
visible_flags: 7

## Flags
- --file <String>: 工作目录内的相对文件路径
- --file-name <String>: 远端显示名称，默认使用本地文件名
- --mime-type <String>: 钉盘上传的 MIME 类型；不能与 --workspace 同时使用
- --space-id <String>: 钉盘空间 ID
- --workspace <String>: 知识库或文档空间 workspaceId；与 --space-id、--mime-type 互斥
- --folder <String>: 目标域内的父文件夹 ID
- --node <String>: 覆盖目标文件 ID

## Related
- dws drive +copy
- dws drive +create-folder
- dws drive +create-shortcut
- dws drive +delete
- dws drive +download
- dws drive +info
