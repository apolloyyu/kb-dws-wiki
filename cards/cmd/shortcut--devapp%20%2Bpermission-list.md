# dws devapp +permission-list

kind: shortcut
completeness: full
description: 查询开放平台应用权限列表
source: internal/shortcut/devapp/devapp.go:1125
visible_flags: 6

## Flags
- --unified-app-id <String>: 开放平台统一应用 ID
- --keyword <String>: 权限名、权限点、接口名关键词
- --scope-value <String>: 精确权限点 scopeValue
- --auth-status <String>: —
- --scope-type <String>: 权限一级类型：APP 或 SNS
- --api-status <String>: 开发者后台 apiStatus 过滤

## Related
- dws devapp +create
- dws devapp +credentials-get
- dws devapp +delete
- dws devapp +disable
- dws devapp +enable
- dws devapp +event-list
