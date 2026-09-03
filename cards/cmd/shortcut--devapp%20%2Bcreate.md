# dws devapp +create

kind: shortcut
completeness: full
usage: dws devapp +create
description: 创建开放平台企业内部应用
source: internal/shortcut/devapp/devapp.go:609
visible_flags: 3

## Flags
- --name <String>: 应用名称
- --desc <String>: 应用描述
- --icon-media-id <String>: 应用图标 mediaId

## Related
- dws devapp +credentials-get
- dws devapp +delete
- dws devapp +disable
- dws devapp +enable
- dws devapp +event-list
- dws devapp +event-subscribe
