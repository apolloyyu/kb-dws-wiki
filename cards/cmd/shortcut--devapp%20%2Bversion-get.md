# dws devapp +version-get

kind: shortcut
completeness: full
usage: dws devapp +version-get
description: 查询指定版本详情
source: internal/shortcut/devapp/devapp.go:2360
visible_flags: 2

## Flags
- --unified-app-id <String>: 开放平台统一应用 ID
- --version-id <String>: 版本 ID

## Related
- dws devapp +create
- dws devapp +credentials-get
- dws devapp +delete
- dws devapp +disable
- dws devapp +enable
- dws devapp +event-list
