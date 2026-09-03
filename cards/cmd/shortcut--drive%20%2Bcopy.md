# dws drive +copy

kind: shortcut
completeness: full
description: 复制文件/文档到指定位置
source: internal/shortcut/drive/drive.go:425
visible_flags: 3

## Flags
- --node <String>: 文档/文件 ID
- --folder <String>: 目标文件夹 nodeId
- --workspace <String>: 目标知识库 ID

## Related
- dws drive +create-folder
- dws drive +create-shortcut
- dws drive +delete
- dws drive +download
- dws drive +info
- dws drive +inspect
