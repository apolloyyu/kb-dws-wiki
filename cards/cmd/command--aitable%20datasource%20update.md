# dws aitable datasource update

kind: command
completeness: full
usage: dws aitable datasource update
description: 更新数据源表同步配置并触发同步
example: dws aitable datasource update --base-id BASE_ID --table-id TABLE_ID --source-config '{"processCode":"PROC-XXXX","name":"采购申请","dataType":"recent_time","recentDays":"30d","iconUrl":"https://example.com/icon.png","url":"https://example.com/oa"}' --auto
source: internal/helpers/aitable.go:9965
visible_flags: 6

## Flags
- --base-id <String>: Base ID (必填)
- --table-id <String>: 数据源表 ID (必填)
- --source-config <String>: 可选。完整源配置 JSON 字符串，显式传入时整体覆盖；省略时先读取当前 sourceConfig 并原样提交，读取失败则不更新
- --auto <Bool>: 可选。是否开启自动同步；仅显式设置时下发给下游，省略时保持原设置
- --field-ids <String>: 不受支持：当前仅支持全量同步，请勿传入
- --auto-sync-setting <String>: 可选。自动同步频率配置 JSON 字符串，仅在显式设置 --auto=true 时生效；省略时保持原有自动同步频率配置。字段：syncType（必填，hourly/scheduled）、hourlyInterval（syncType=hourly 时必填）、scheduleType（syncType=scheduled

## Related
- dws aitable datasource create
- dws aitable datasource get-config
- dws aitable datasource get-fields
- dws aitable datasource list-sources
- dws aitable datasource sync
- dws aitable datasource sync-status
