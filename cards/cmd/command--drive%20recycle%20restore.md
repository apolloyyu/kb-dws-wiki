# dws drive recycle restore

kind: command
completeness: full
usage: dws drive recycle restore
description: 还原回收站中的文件
example: dws drive recycle restore --id RECYCLE_ITEM_ID
source: internal/helpers/drive.go:3365
visible_flags: 1

## Flags
- --id <String>: 回收项 ID (必填，从 recycle list 获取)

## Related
- dws drive recycle list
