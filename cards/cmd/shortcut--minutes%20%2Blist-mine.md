# dws minutes +list-mine

kind: shortcut
completeness: full
usage: dws minutes +list-mine
description: 查询我创建的听记列表
source: internal/shortcut/minutes/minutes.go:38
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
- dws minutes +list-shared
- dws minutes +mindmap
