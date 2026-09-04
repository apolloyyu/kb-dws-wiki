# dws aitable datasource sync

kind: command
completeness: full
usage: dws aitable datasource sync
description: 触发数据源表手动同步
example: dws aitable datasource sync --base-id BASE_ID --table-ids TBL1,TBL2
source: internal/helpers/aitable.go:8824
visible_flags: 2

## Flags
- --base-id <String>: Base ID (必填)
- --table-ids <String>: 待触发同步的数据源表 ID 列表，逗号分隔，1-5 个 (必填)

## Related
- dws aitable datasource create
- dws aitable datasource get-config
- dws aitable datasource get-fields
- dws aitable datasource list-sources
- dws aitable datasource sync-status
- dws aitable datasource update
