# dws minutes +list-all

kind: shortcut
completeness: full
usage: dws minutes +list-all
description: 预览或完整查询我有权限访问的听记列表
source: internal/shortcut/minutes/minutes.go:138
visible_flags: 5

## Flags
- --query <String>: 关键字筛选
- --limit <Int>: —
- --cursor <String>: 单端点预览的分页 token；不能与 --page-all 同用
- --page-all <Bool>: 分别追完 mine/shared 并合并 accessible 全集
- --page-limit <Int>: —

## Related
- dws minutes +apply-permission
- dws minutes +download
- dws minutes +export-pack
- dws minutes +list-mine
- dws minutes +list-shared
- dws minutes +mindmap
