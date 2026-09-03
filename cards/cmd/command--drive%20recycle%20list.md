# dws drive recycle list

kind: command
completeness: full
usage: dws drive recycle list
description: 查看回收站文件列表
example: dws drive recycle list
source: internal/helpers/drive.go:3301
visible_flags: 3

## Flags
- --space-id <String>: 钉盘空间 ID (选填，不传则返回所有空间)
- --limit <Int>: 返回条数上限 (默认20，最大50)
- --cursor <String>: 分页游标

## Related
- dws drive recycle restore
