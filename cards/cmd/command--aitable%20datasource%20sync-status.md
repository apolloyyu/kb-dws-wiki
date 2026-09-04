# dws aitable datasource sync-status

kind: command
completeness: full
usage: dws aitable datasource sync-status
description: 按任务 ID 查询数据源同步任务状态
example: dws aitable datasource sync-status --base-id BASE_ID --table-id TABLE_ID --task-ids TASK1,TASK2
source: internal/helpers/aitable.go:8873
visible_flags: 3

## Flags
- --base-id <String>: Base ID (必填)
- --table-id <String>: 数据源表 ID (必填)
- --task-ids <String>: 待查询的同步任务 ID 列表，逗号分隔，1-5 个 (必填)

## Related
- dws aitable datasource create
- dws aitable datasource get-config
- dws aitable datasource get-fields
- dws aitable datasource list-sources
- dws aitable datasource sync
- dws aitable datasource update
