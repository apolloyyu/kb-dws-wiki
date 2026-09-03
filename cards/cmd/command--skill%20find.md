# dws skill find

kind: command
completeness: full
description: 兼容旧用法，提示使用 skill search
source: internal/helpers/chat.go:8698
visible_flags: 3

## Flags
- --query <String>: 搜索关键词 (必填)
- --limit <Int>: 每页返回数量（默认 20）
- --cursor <String>: 分页游标（首次调用不传，翻页时传上次返回的 nextCursor）

## Related
- dws skill add
- dws skill get
- dws skill install
- dws skill search
- dws skill setup
