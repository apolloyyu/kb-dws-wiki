# dws aitable workflow list

kind: command
completeness: full
usage: dws aitable workflow list
description: 列出 Base 下的工作流
example: dws aitable workflow list --base-id BASE_ID
source: internal/helpers/aitable.go:5990
visible_flags: 3

## Flags
- --base-id <String>: 目标 Base ID (必填)
- --limit <Int>: 分页大小 [1, 100]，不传走服务端默认 20
- --offset <Int>: 分页偏移量，>= 0，不传走服务端默认 0

## Related
- dws aitable workflow create
- dws aitable workflow disable
- dws aitable workflow edit-example
- dws aitable workflow enable
- dws aitable workflow get
- dws aitable workflow history
