# dws drive comment create

kind: command
completeness: full
description: 创建文件夹（deprecated）
source: internal/helpers/drive.go:3410
visible_flags: 3

## Flags
- --name <String>: 文件夹名称（必填）
- --folder <String>: 父文件夹 nodeId 或 URL
- --workspace <String>: 目标知识库 ID

## Related
- dws drive comment list
