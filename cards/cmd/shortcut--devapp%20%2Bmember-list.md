# dws devapp +member-list

kind: shortcut
completeness: full
usage: dws devapp +member-list
description: 查询开放平台应用成员
source: internal/shortcut/devapp/devapp.go:1294
visible_flags: 2

## Flags
- --unified-app-id <String>: 开放平台统一应用 ID
- --user-id <String>: 可选稳定 userId；由 Shortcut 在严格验证完整成员数组后做精确等值筛选

## Related
- dws devapp +create
- dws devapp +credentials-get
- dws devapp +delete
- dws devapp +disable
- dws devapp +enable
- dws devapp +event-list
