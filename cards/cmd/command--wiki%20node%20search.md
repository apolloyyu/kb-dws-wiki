# dws wiki node search

kind: command
completeness: full
usage: dws wiki node search
description: 在知识库中搜索节点
example: dws wiki node search --workspace <workspaceId> --query "产品方案"
source: internal/helpers/wiki.go:1333
visible_flags: 5

## Flags
- --workspace <String>: 知识库 ID (必填)
- --query <String>: 搜索关键词 (必填)
- --extensions <StringSlice>: 按文件扩展名过滤 (如 adoc,asheet,pdf)
- --limit <Int>: 每页数量 (默认 10，最大 30)
- --cursor <String>: 分页游标

## Related
- dws wiki node copy
- dws wiki node create
- dws wiki node delete
- dws wiki node list
- dws wiki node move
