# dws devapp +permission-add

kind: shortcut
completeness: full
usage: dws devapp +permission-add
description: 申请开放平台应用权限点
source: internal/shortcut/devapp/devapp.go:1248
visible_flags: 2

## Flags
- --unified-app-id <String>: 开放平台统一应用 ID
- --scope-values <StringSlice>: 权限点 scopeValue 列表

## Related
- dws devapp +create
- dws devapp +credentials-get
- dws devapp +delete
- dws devapp +disable
- dws devapp +enable
- dws devapp +event-list
