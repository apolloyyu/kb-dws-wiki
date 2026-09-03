# dws aitable +field-get

kind: shortcut
completeness: full
description: 批量获取字段详情（含类型相关完整配置）
source: internal/shortcut/aitable/aitable.go:556
visible_flags: 3

## Flags
- --base-id <String>: Base ID
- --table-id <String>: Table ID
- --field-ids <StringSlice>: 字段 ID 列表，逗号分隔，单次最多 10 个（可选）

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
