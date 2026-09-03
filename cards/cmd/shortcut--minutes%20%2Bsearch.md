# dws minutes +search

kind: shortcut
completeness: full
description: 按范围、标题关键词和时间搜索听记，支持安全全量翻页
source: internal/shortcut/minutes/alignment.go:31
visible_flags: 8

## Flags
- --query <String>: 标题关键词；shortcut 会对后端结果再次精确包含过滤
- --scope <String>: —
- --start <String>: 开始时间 RFC3339
- --end <String>: 结束时间 RFC3339
- --limit <Int>: —
- --cursor <String>: 起始 nextToken
- --page-all <Bool>: 自动读取全部页
- --page-limit <Int>: —

## Related
- dws minutes +apply-permission
- dws minutes +download
- dws minutes +export-pack
- dws minutes +list-all
- dws minutes +list-mine
- dws minutes +list-shared
