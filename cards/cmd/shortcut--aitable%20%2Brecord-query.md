# dws aitable +record-query

kind: shortcut
completeness: full
description: 查询表格记录（按 ID / 条件 / 关键词，并支持字段投影和分页）
source: internal/shortcut/aitable/aitable.go:680
visible_flags: 9

## Flags
- --base-id <String>: Base ID
- --table-id <String>: Table ID
- --record-ids <StringSlice>: 记录 ID 列表，单次最多 100（可选）
- --field-ids <StringSlice>: 返回字段 ID 列表（可选）
- --filters <String>: 结构化过滤条件 JSON（可选）
- --sort <String>: 排序条件 JSON 数组（可选）
- --query <String>: 全文关键词（可选）
- --limit <Int>: 单次最大记录数，默认 100（可选）
- --cursor <String>: 分页游标（可选）

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
