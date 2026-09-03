# dws aitable +datasource-list-sources

kind: shortcut
completeness: full
usage: dws aitable +datasource-list-sources
description: 列出指定 Base 下可用的数据源条目。仅支持 OA 审批数据源（datasourceType=OA）。返回的每条条目包含 result 字段（下游原始 JSON 字符串）和 sourceType 字段（OA 审批对应 2，仅供参考）。OA 审批场景下 result 为包含 approvals 数组的 JSON 字符串
source: internal/shortcut/aitable/datasource.go:406
visible_flags: 2

## Flags
- --base-id <String>: 目标 Base ID
- --datasource-type <String>: 数据源类型，目前支持审批（OA）

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
