# dws devapp +event-unsubscribe

kind: shortcut
completeness: full
usage: dws devapp +event-unsubscribe
description: 取消订阅应用事件
source: internal/shortcut/devapp/devapp.go:2112
visible_flags: 2

## Flags
- --unified-app-id <String>: 开放平台统一应用 ID
- --event-codes <StringSlice>: 事件码列表

## Related
- dws devapp +create
- dws devapp +credentials-get
- dws devapp +delete
- dws devapp +disable
- dws devapp +enable
- dws devapp +event-list
