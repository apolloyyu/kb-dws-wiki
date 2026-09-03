# dws aitable datasource list-sources

kind: command
completeness: full
usage: dws aitable datasource list-sources
description: 列出可用数据源来源
example: dws aitable datasource list-sources --base-id BASE_ID --datasource-type OA
source: internal/helpers/aitable.go:8555
visible_flags: 2

## Flags
- --base-id <String>: Base ID (必填)
- --datasource-type <String>: 数据源类型，目前支持 OA (必填)

## Related
- dws aitable datasource create
- dws aitable datasource get-config
- dws aitable datasource get-fields
- dws aitable datasource sync
- dws aitable datasource sync-status
- dws aitable datasource update
