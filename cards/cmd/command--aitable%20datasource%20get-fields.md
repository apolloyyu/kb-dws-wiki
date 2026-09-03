# dws aitable datasource get-fields

kind: command
completeness: full
description: 获取数据源可同步字段列表
source: internal/helpers/aitable.go:8610
visible_flags: 3

## Flags
- --base-id <String>: Base ID (必填)
- --datasource-type <String>: 数据源类型，目前支持 OA (必填)
- --source-config <String>: 源配置 JSON 字符串，需含 processCode、name、iconUrl、url、dataType 及对应时间字段 (必填)

## Related
- dws aitable datasource create
- dws aitable datasource get-config
- dws aitable datasource list-sources
- dws aitable datasource sync
- dws aitable datasource sync-status
- dws aitable datasource update
