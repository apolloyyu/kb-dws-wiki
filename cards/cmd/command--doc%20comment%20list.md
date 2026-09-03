# dws doc comment list

kind: command
completeness: full
usage: dws doc comment list
description: List comments on a DingTalk Doc, including replies.
example: dws doc comment list --node DOC_ID
use_when: When the agent is reviewing outstanding feedback or summarizing comment threads.
source: internal/helpers/doc.go:3077
visible_flags: 5

## Flags
- --node <String>: 目标文档的标识，支持传入 URL 或 ID (必填)
- --limit <Int>: 每页返回的评论数量，默认 50，最大 50
- --cursor <String>: 分页游标，从上一次请求的返回结果中获取 (首次请求不传)
- --type <String>: 按评论类型过滤: global (全文评论) / inline (划词评论)
- --resolve-status <String>: 按解决状态过滤: resolved (已解决) / unresolved (未解决)

## Related
- dws doc comment create
- dws doc comment create-inline
- dws doc comment delete
- dws doc comment reply
- dws doc comment update
