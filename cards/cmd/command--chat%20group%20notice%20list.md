# dws chat group notice list

kind: command
completeness: full
usage: dws chat group notice list
description: 查看群公告列表
example: dws chat group notice list --conversation-id <openConversationId>
source: internal/helpers/chat.go:10823
visible_flags: 4

## Flags
- --conversation-id <String> required: 群聊 openConversationId (必填)
- --limit <Int>: 每页返回数量（默认 10，最大 100）
- --cursor <String>: 分页游标（首次不传，翻页传返回的 nextPageCursor）
- --scheduled <Bool>: 是否查询定时公告列表（默认 false，查询已发布公告）

## Related
- dws chat group notice create
- dws chat group notice edit
- dws chat group notice get
