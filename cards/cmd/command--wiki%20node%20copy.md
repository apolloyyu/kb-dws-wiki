# dws wiki node copy

kind: command
completeness: full
description: 复制知识库节点
source: internal/helpers/wiki.go:1134
visible_flags: 3

## Flags
- --workspace <String>: 知识库 ID (必填)
- --node <String>: 源节点 ID (必填)
- --folder <String>: 目标文件夹 nodeId (选填)

## Related
- dws wiki node create
- dws wiki node delete
- dws wiki node list
- dws wiki node move
- dws wiki node search
