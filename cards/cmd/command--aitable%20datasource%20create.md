# dws aitable datasource create

kind: command
completeness: full
usage: dws aitable datasource create
description: 创建数据源表并触发首次同步
example: dws aitable datasource create --base-id BASE_ID --datasource-type OA --source-config '{"processCode":"PROC-XXXX","name":"采购申请","dataType":"recent_time","recentDays":"30d","iconUrl":"https://example.com/icon.png","url":"https://example.com/oa"}'
source: internal/helpers/aitable.go:8668
visible_flags: 6

## Flags
- --base-id <String>: Base ID (必填)
- --datasource-type <String>: 数据源类型，目前支持 OA (必填)
- --source-config <String>: 源配置 JSON 字符串，须从 list-sources 原样透传 processCode/name/iconUrl/url，并设置 dataType 及对应时间字段 (必填)
- --auto <Bool>: 是否开启自动同步，默认 false；创建新数据源表时始终下发给下游
- --field-ids <String>: 需要同步的字段 ID 列表，逗号分隔；不传时同步全部字段
- --auto-sync-setting <String>: 自动同步频率配置 JSON 字符串，仅在 --auto=true 时生效。字段：syncType（必填，hourly/scheduled）、hourlyInterval（syncType=hourly 时必填）、scheduleType（syncType=scheduled 时必填，daily/weekly/month

## Related
- dws aitable datasource get-config
- dws aitable datasource get-fields
- dws aitable datasource list-sources
- dws aitable datasource sync
- dws aitable datasource sync-status
- dws aitable datasource update
