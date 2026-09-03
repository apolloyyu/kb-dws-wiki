# dws aitable datasource get-config

kind: command
completeness: full
usage: dws aitable datasource get-config
description: 获取数据源表同步配置
example: dws aitable datasource get-config --base-id BASE_ID --table-id TABLE_ID
source: internal/helpers/aitable.go:8514
visible_flags: 2

## Flags
- --base-id <String>: Base ID (必填)
- --table-id <String>: 数据源表 ID (必填)

## Related
- dws aitable datasource create
- dws aitable datasource get-fields
- dws aitable datasource list-sources
- dws aitable datasource sync
- dws aitable datasource sync-status
- dws aitable datasource update
