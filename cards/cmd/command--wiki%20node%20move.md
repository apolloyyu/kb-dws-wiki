# dws wiki node move

kind: command
completeness: full
description: 移动知识库节点
source: internal/helpers/wiki.go:1204
visible_flags: 3

## Flags
- --workspace <String>: 知识库 ID (必填)
- --node <String>: 源节点 ID (必填)
- --folder <String>: 目标文件夹 nodeId (选填)

## Related
- dws wiki node copy
- dws wiki node create
- dws wiki node delete
- dws wiki node list
- dws wiki node search
