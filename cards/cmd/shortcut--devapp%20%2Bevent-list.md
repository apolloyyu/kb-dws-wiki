# dws devapp +event-list

kind: shortcut
completeness: full
description: 查询应用可用事件目录与订阅状态
source: internal/shortcut/devapp/devapp.go:1881
visible_flags: 2

## Flags
- --unified-app-id <String>: 开放平台统一应用 ID
- --keyword <String>: 事件搜索关键词，支持按事件码或事件名称模糊匹配

## Related
- dws devapp +create
- dws devapp +credentials-get
- dws devapp +delete
- dws devapp +disable
- dws devapp +enable
- dws devapp +event-subscribe
