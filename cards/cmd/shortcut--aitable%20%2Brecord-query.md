# dws aitable +record-query

kind: shortcut
completeness: partial
usage: dws aitable +record-query
description: —
source: internal/shortcut/aitable/aitable.go:699
visible_flags: 13
partial_reason: missing_description

## Flags
- --base-id <String>: Base ID
- --table-id <String>: Table ID
- --record-ids <StringSlice>: 记录 ID 列表，单次最多 100（可选）
- --field-ids <StringSlice>: 返回字段 ID 列表（可选）；必须先通过 field get 获取真实 fieldId，不要传字段中文名
- --filters <String>: —
- --sort <String>: 排序条件 JSON 数组（可选）；fieldId 必须来自 field get，direction 仅用 asc/desc
- --query <String>: 全文关键词（可选）
- --limit <Int>: 默认单次最大记录数 100；--all 时作为每个请求的页大小，上限 20（可选）
- … 5 more; use dwsdoc cmd/short for full flags

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
