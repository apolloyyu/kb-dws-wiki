# dws aitable record query

kind: command
completeness: partial
usage: dws aitable record query
description: Query records from a datasheet with optional filters, sort, view scoping, and pagination.
example: dws aitable record query --base-id BASE_ID --table-id TABLE_ID
use_when: When the agent needs to read row data to reason about it, render it, or feed it into downstream logic.
source: internal/helpers/aitable.go:2670
visible_flags: 11
partial_reason: unverified_flags

## Flags
- --base-id <String>: Base ID（通过 base list / base search 获取）(必填)
- --table-id <String>: Table ID（通过 base get 获取）(必填)
- --record-ids <String>: 指定要获取的记录 ID 列表，逗号分隔，单次最多 100 个。传入时按 ID 返回，忽略 filters 和 sort。适用于已知 recordId（如关联字段中的 linkedRecordIds）时的精准取数
- --field-ids <String>: 指定要返回的字段 ID 列表，逗号分隔。省略则返回所有字段。建议在字段较多时按需传入，可显著减少响应体积；单次最多 100 个
- --filters <String>: 结构化过滤条件 JSON，不传则返回全部记录（受 limit 限制）
- --sort <String>: 排序条件 JSON 数组，按数组顺序依次生效
- --query <String>: 全文关键词。将对整表内容做文本匹配搜索，并返回符合条件的记录
- --limit <Int>: 单次返回的最大记录数，默认 100，最大 100
- … 3 more; use dwsdoc cmd/short for full flags

## Related
- dws aitable record batch-update
- dws aitable record create
- dws aitable record delete
- dws aitable record get
- dws aitable record group-stats
- dws aitable record history-list
