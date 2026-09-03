# dws aitable record query

kind: command
completeness: full
description: Query records from a datasheet with optional filters, sort, view scoping, and pagination.
use_when: When the agent needs to read row data to reason about it, render it, or feed it into downstream logic.
source: internal/helpers/aitable.go:2670
visible_flags: 11

## Flags
- --base-id <String>: Base ID（通过 base list / base search 获取）(必填)
- --table-id <String>: Table ID（通过 base get 获取）(必填)
- --record-ids <String>: 指定要获取的记录 ID 列表，逗号分隔，单次最多 100 个。传入时按 ID 返回，忽略 filters 和 sort。适用于已知 recordId（如关联字段中的 linkedRecordIds）时的精准取数
- --field-ids <String>: 指定要返回的字段 ID 列表，逗号分隔。省略则返回所有字段。建议在字段较多时按需传入，可显著减少响应体积；单次最多 100 个
- --filters <String>: 结构化过滤条件 JSON，不传则返回全部记录（受 limit 限制）
- --sort <String>: 排序条件 JSON 数组，按数组顺序依次生效
- --query <String>: 全文关键词。将对整表内容做文本匹配搜索，并返回符合条件的记录
- --limit <Int>: 单次返回的最大记录数，默认 100，最大 100
- --cursor <String>: 分页游标，首次查询不传；cursor 为空表示已取完全部记录
- --all <Bool>: 自动翻页获取完整记录集；达到 --page-limit 且仍有更多页时返回非零结构化错误，不把不完整结果作为成功输出
- --page-limit <Int>: 自动翻页最大页数（仅 --all 时生效）。默认 50 页（约 5000 条）；设为 0 表示显式不限页数；超限时错误详情保留已取记录和续传 cursor

## Related
- dws aitable record batch-update
- dws aitable record create
- dws aitable record delete
- dws aitable record get
- dws aitable record group-stats
- dws aitable record history-list
