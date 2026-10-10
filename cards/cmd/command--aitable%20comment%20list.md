# dws aitable comment list

kind: command
completeness: partial
usage: dws aitable comment list
description: —
source: internal/helpers/aitable_comment.go:65
visible_flags: 2
partial_reason: unverified_flags,missing_description

## Flags
- --limit <Int>: 每次检查的底层评论数量，范围 1-100，默认 50
- --cursor <String>: 上一次相同 Base、数据表和记录查询返回的 meta.pagination.next_token

## Related
- dws aitable comment create
- dws aitable comment delete
- dws aitable comment reply
- dws aitable comment update
