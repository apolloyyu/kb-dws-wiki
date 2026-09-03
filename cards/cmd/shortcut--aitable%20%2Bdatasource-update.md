# dws aitable +datasource-update

kind: shortcut
completeness: full
usage: dws aitable +datasource-update
description: 更新指定 AI 表格中已有数据源表的同步配置，支持更新源配置、自动同步开关和同步字段选择。更新后触发一次同步。仅适用于数据源表。
source: internal/shortcut/aitable/datasource.go:125
visible_flags: 6

## Flags
- --base-id <String>: 目标 Base ID
- --table-id <String>: 已存在的数据源表 ID（通过 +base-get / +table-list 获取，仅允许传入 sync=true 的数据源表）
- --source-config <String>: 可选。新的源配置 JSON 字符串。不传时保持原有配置不变；传入时整体覆盖。字段分为两类：须从 +datasource-list-sources 结果原样透传的字段（必填）：processCode（审批流程编码）、name（展示名称）、ic
- --auto <Bool>: 可选。是否开启自动同步；仅显式设置时下发给下游，省略时保持原有自动同步开关不变
- --field-ids <StringSlice>: 需要同步的字段 ID 列表，不传时保持现有配置（创建时默认为全部字段）
- --auto-sync-setting <String>: 可选。自动同步频率配置 JSON 字符串，仅在显式设置 --auto=true 时生效；省略时保持原有自动同步频率配置。字段：syncType（必填，hourly=按小时间隔，scheduled=定时触发）、hourlyInterval（s

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
