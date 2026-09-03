# dws drive shortcut

kind: command
completeness: full
description: 为节点创建快捷方式
source: internal/helpers/drive.go:2447
visible_flags: 3

## Flags
- --node <String>: 源节点 ID 或文档 URL (必填)
- --folder <String>: 目标文件夹 nodeId (可选)
- --workspace <String>: 目标知识库 ID (可选)

## Related
- dws drive comment
- dws drive commit
- dws drive copy
- dws drive cover
- dws drive delete
- dws drive download
