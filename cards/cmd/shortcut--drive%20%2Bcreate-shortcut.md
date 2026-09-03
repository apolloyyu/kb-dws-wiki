# dws drive +create-shortcut

kind: shortcut
completeness: full
usage: dws drive +create-shortcut
description: 为已有节点创建快捷方式并验证新节点
source: internal/shortcut/drive/operations.go:167
visible_flags: 3

## Flags
- --node <String>: 源节点 ID
- --folder <String>: 目标文件夹 ID
- --workspace <String>: 目标知识库 ID

## Related
- dws drive +copy
- dws drive +create-folder
- dws drive +delete
- dws drive +download
- dws drive +info
- dws drive +inspect
