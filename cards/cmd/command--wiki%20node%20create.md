# dws wiki node create

kind: command
completeness: full
usage: dws wiki node create
description: 在知识库中创建节点
example: dws wiki node create --workspace <workspaceId> --name "新文档"
source: internal/helpers/wiki.go:1049
visible_flags: 4

## Flags
- --workspace <String>: 知识库 ID (必填)
- --name <String>: 节点名称 (必填)
- --type <String>: 节点类型: adoc / axls / able / appt / adraw / amind / folder（asheet 不支持）
- --folder <String>: 父节点 nodeId (选填，不传则在根目录创建)

## Related
- dws wiki node copy
- dws wiki node delete
- dws wiki node list
- dws wiki node move
- dws wiki node search
