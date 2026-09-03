# dws minutes +update

kind: shortcut
completeness: full
usage: dws minutes +update
description: 读取现状、预览差异、更新听记标题并读回验证
source: internal/shortcut/minutes/alignment.go:166
visible_flags: 2

## Flags
- --id <String>: 听记 taskUuid
- --title <String>: 新标题

## Related
- dws minutes +apply-permission
- dws minutes +download
- dws minutes +export-pack
- dws minutes +list-all
- dws minutes +list-mine
- dws minutes +list-shared
