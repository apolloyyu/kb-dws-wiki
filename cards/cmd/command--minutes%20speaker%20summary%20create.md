# dws minutes speaker summary create

kind: command
completeness: full
usage: dws minutes speaker summary create
description: 触发创建发言人段落总结任务
example: dws minutes speaker summary create --ids <uuid1,uuid2>
source: internal/helpers/minutes.go:1138
visible_flags: 1

## Flags
- --ids <String>: 听记 taskUuid 列表，逗号分隔 (必填)

## Related
- dws minutes speaker summary get
