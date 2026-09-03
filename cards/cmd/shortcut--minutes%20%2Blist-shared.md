# dws minutes +list-shared

kind: shortcut
completeness: full
description: 查询他人共享给我的听记列表
source: internal/shortcut/minutes/minutes.go:88
visible_flags: 5

## Flags
- --query <String>: 关键字筛选
- --limit <Int>: —
- --cursor <String>: 分页 token (首页留空)
- --page-all <Bool>: 自动读取该范围全部分页
- --page-limit <Int>: —

## Related
- dws minutes +apply-permission
- dws minutes +download
- dws minutes +export-pack
- dws minutes +list-all
- dws minutes +list-mine
- dws minutes +mindmap
