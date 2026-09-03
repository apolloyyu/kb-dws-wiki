# dws chat group list-all

kind: command
completeness: full
usage: dws chat group list-all
description: 分页拉取我所有群列表
example: dws chat group list-all
source: internal/helpers/chat.go:9388
visible_flags: 2

## Flags
- --limit <Int>: 每页返回数量（默认 100，最大 200）
- --cursor <String>: 分页游标（首次不传，翻页传返回的 nextCursor）

## Related
- dws chat group audit-join-validation
- dws chat group bots
- dws chat group create
- dws chat group dismiss
- dws chat group get-by-group-id
- dws chat group get-mute-config
