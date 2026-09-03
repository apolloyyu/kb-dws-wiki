# dws aitable +datasource-get-fields

kind: shortcut
completeness: full
usage: dws aitable +datasource-get-fields
description: 获取指定数据源下可供同步的字段列表，用于在 +datasource-create / +datasource-update 中决定同步哪些字段。传入从 +datasource-list-sources 获取的 sourceConfig。仅支持 OA 审批数据源（datasourceType=OA），其他数据源类型暂不支
source: internal/shortcut/aitable/datasource.go:464
visible_flags: 3

## Flags
- --base-id <String>: 目标 Base ID
- --datasource-type <String>: 数据源类型，目前支持审批（OA）
- --source-config <String>: 源配置 JSON 字符串。结构同 +datasource-create 的 --source-config，需含 processCode、name、iconUrl、url、dataType 及对应时间字段

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
