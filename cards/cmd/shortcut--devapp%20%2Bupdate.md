# dws devapp +update

kind: shortcut
completeness: full
description: 修改开放平台企业内部应用基础信息
source: internal/shortcut/devapp/devapp.go:692
visible_flags: 4

## Flags
- --unified-app-id <String>: 开放平台统一应用 ID
- --name <String>: 新的应用名称；至少提供一项非空的应用基础信息更新
- --desc <String>: 新的应用描述；至少提供一项非空的应用基础信息更新
- --icon-media-id <String>: 新的应用图标 mediaId；至少提供一项非空的应用基础信息更新

## Related
- dws devapp +create
- dws devapp +credentials-get
- dws devapp +delete
- dws devapp +disable
- dws devapp +enable
- dws devapp +event-list
