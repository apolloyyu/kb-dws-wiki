# dws minutes speaker summary get

kind: command
completeness: full
usage: dws minutes speaker summary get
description: 查询发言人段落总结结果
example: dws minutes speaker summary get --ids <uuid1,uuid2>
source: internal/helpers/minutes.go:1193
visible_flags: 1

## Flags
- --ids <String>: 听记 taskUuid 列表，逗号分隔 (必填)

## Related
- dws minutes speaker summary create
