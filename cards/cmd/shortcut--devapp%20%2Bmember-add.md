# dws devapp +member-add

kind: shortcut
completeness: full
description: 添加开放平台应用成员
source: internal/shortcut/devapp/devapp.go:1423
visible_flags: 3

## Flags
- --unified-app-id <String>: 开放平台统一应用 ID
- --user-ids <StringSlice>: 成员 userId 列表，不能为空且不能重复
- --member-type <String>: 成员类型，如 DEVELOPER，不能为空

## Related
- dws devapp +create
- dws devapp +credentials-get
- dws devapp +delete
- dws devapp +disable
- dws devapp +enable
- dws devapp +event-list
