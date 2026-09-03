# dws drive +inspect

kind: shortcut
completeness: full
description: 聚合检查节点元数据及可选统计、公开状态和封面
source: internal/shortcut/drive/operations.go:16
visible_flags: 5

## Flags
- --node <String>: 节点 ID
- --space-id <String>: 钉盘空间 ID
- --include-stats <Bool>: 附带阅读、编辑、下载等统计
- --include-publish <Bool>: 附带互联网公开状态
- --include-cover <Bool>: 附带封面或缩略图地址

## Related
- dws drive +copy
- dws drive +create-folder
- dws drive +create-shortcut
- dws drive +delete
- dws drive +download
- dws drive +info
