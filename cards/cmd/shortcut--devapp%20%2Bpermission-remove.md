# dws devapp +permission-remove

kind: shortcut
completeness: full
usage: dws devapp +permission-remove
description: 取消开放平台应用权限点
source: internal/shortcut/devapp/devapp.go:1269
visible_flags: 2

## Flags
- --unified-app-id <String>: 开放平台统一应用 ID
- --scope-values <StringSlice>: 待取消权限点 scopeValue 列表

## Related
- dws devapp +create
- dws devapp +credentials-get
- dws devapp +delete
- dws devapp +disable
- dws devapp +enable
- dws devapp +event-list
