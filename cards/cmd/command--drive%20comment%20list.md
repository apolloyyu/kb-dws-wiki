# dws drive comment list

kind: command
completeness: partial
usage: dws drive comment list
description: —
source: internal/helpers/file_comment.go:85
visible_flags: 4
partial_reason: unverified_flags,missing_description

## Flags
- --limit <Int>: 每页评论数，范围 1-200
- --cursor <String>: 分页游标，取自上页 nextCursor
- --all <Bool>: 自动拉取全部评论，最多 10 页 / 2000 条
- --scope <String>: 评论范围: all(全部) / whole(全文) / partial(历史局部)(可选: all|whole|partial)

## Related
- dws drive comment create
