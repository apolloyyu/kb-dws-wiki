# dws agoal obj-template list

kind: command
completeness: full
usage: dws agoal obj-template list
description: 获取目标模板列表
example: dws agoal obj-template list
source: internal/helpers/agoal.go:525
visible_flags: 4

## Flags
- --request-id <String>: requestId (可选)
- --page <Int>: 页码，默认 1 (可选)
- --page-size <Int>: 每页数量，默认 10 (可选)
- --keyword <String>: 搜索关键词 (可选)

## Related
- dws agoal obj-template create-or-update
