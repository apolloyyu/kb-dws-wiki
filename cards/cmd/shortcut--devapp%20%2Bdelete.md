# dws devapp +delete

kind: shortcut
completeness: full
usage: dws devapp +delete
description: 删除开放平台企业内部应用（不可逆）
source: internal/shortcut/devapp/devapp.go:780
visible_flags: 1

## Flags
- --unified-app-id <String>: 开放平台统一应用 ID

## Related
- dws devapp +create
- dws devapp +credentials-get
- dws devapp +disable
- dws devapp +enable
- dws devapp +event-list
- dws devapp +event-subscribe
