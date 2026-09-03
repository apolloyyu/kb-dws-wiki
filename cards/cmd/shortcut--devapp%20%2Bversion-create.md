# dws devapp +version-create

kind: shortcut
completeness: full
usage: dws devapp +version-create
description: 基于当前配置创建应用新版本
source: internal/shortcut/devapp/devapp.go:2137
visible_flags: 3

## Flags
- --unified-app-id <String>: 开放平台统一应用 ID
- --version <String>: 高级可选：显式版本号，如 1.0.1；默认由服务端自动递增
- --desc <String>: 版本描述

## Related
- dws devapp +create
- dws devapp +credentials-get
- dws devapp +delete
- dws devapp +disable
- dws devapp +enable
- dws devapp +event-list
