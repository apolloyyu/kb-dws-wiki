# dws wiki node delete

kind: command
completeness: full
usage: dws wiki node delete
description: 删除知识库节点
example: dws wiki node delete --workspace <workspaceId> --node <nodeId>
source: internal/helpers/wiki.go:1273
visible_flags: 2

## Flags
- --workspace <String>: 知识库 ID (必填，用于权限校验)
- --node <String>: 节点 ID (必填)

## Related
- dws wiki node copy
- dws wiki node create
- dws wiki node list
- dws wiki node move
- dws wiki node search
