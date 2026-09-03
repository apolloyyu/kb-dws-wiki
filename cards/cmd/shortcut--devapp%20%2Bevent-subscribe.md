# dws devapp +event-subscribe

kind: shortcut
completeness: full
usage: dws devapp +event-subscribe
description: 订阅应用事件回调
source: internal/shortcut/devapp/devapp.go:1983
visible_flags: 2

## Flags
- --unified-app-id <String>: 开放平台统一应用 ID
- --event-codes <StringSlice>: 事件码列表至少包含一项非空且互不重复的 eventCode

## Related
- dws devapp +create
- dws devapp +credentials-get
- dws devapp +delete
- dws devapp +disable
- dws devapp +enable
- dws devapp +event-list
