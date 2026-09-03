# dws aitable +datasource-create

kind: shortcut
completeness: full
description: 为指定 AI 表格创建数据源同步配置，创建一张数据源表并触发首次全量同步。返回新建数据源表 ID 和同步任务 ID。
source: internal/shortcut/aitable/datasource.go:38
visible_flags: 6

## Flags
- --base-id <String>: 目标 Base ID（通过 +base-list / +base-search 获取）
- --datasource-type <String>: 数据源类型，目前支持审批（OA）
- --source-config <String>: 源配置 JSON 字符串。字段分为两类：须从 +datasource-list-sources 结果原样透传的字段（必填）：processCode（审批流程编码）、name（展示名称）、iconUrl（图标 URL）、url（跳转链接）；调
- --auto <Bool>: 是否开启自动同步，默认 false；创建新数据源表时该字段始终下发给下游
- --field-ids <StringSlice>: 需要同步的字段 ID 列表，不传时保持现有配置（创建时默认为全部字段）
- --auto-sync-setting <String>: 自动同步频率配置 JSON 字符串，仅在 --auto=true 时生效。字段：syncType（必填，hourly=按小时间隔，scheduled=定时触发）、hourlyInterval（syncType=hourly 时必填，正整数小

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
