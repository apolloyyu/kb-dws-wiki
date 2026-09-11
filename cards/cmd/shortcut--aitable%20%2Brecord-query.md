# dws aitable +record-query

kind: shortcut
completeness: full
usage: dws aitable +record-query
description: Base ID
source: internal/shortcut/aitable/aitable.go:700
visible_flags: 9

## Flags
- --base-id <String>: Base ID
- --table-id <String>: Table ID
- --record-ids <StringSlice>: 记录 ID 列表，单次最多 100（可选）
- --field-ids <StringSlice>: 返回字段 ID 列表（可选）；必须先通过 field get 获取真实 fieldId，不要传字段中文名
- --filters <String>: 结构化过滤条件 JSON（可选）；先用 field get 完整读一遍表头，确定用户条件对应的字段和类型后再传值。日期值用日期字符串或毫秒数，不接受 View relative/exact Scheme。人员、部门、群组禁止原值透传，必须分
- --sort <String>: 排序条件 JSON 数组（可选）；fieldId 必须来自 field get，direction 仅用 asc/desc
- --query <String>: 全文关键词（可选）
- --limit <Int>: 单次最大记录数，默认 100（可选）
- --cursor <String>: 分页游标（可选）；首次不传，后续只能原样使用上一页 data.nextCursor，并保持全部查询条件不变；普通扫描满 limit 后成功返回空续页属于正常情况，records 为空时仍以 nextCursor 是否为空判断继续或完成；不得

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
