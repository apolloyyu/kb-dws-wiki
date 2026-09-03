# dws devapp +version-publish

kind: shortcut
completeness: full
usage: dws devapp +version-publish
description: 发布指定版本（含高敏权限需 --confirmed-sensitive）
source: internal/shortcut/devapp/devapp.go:2472
visible_flags: 4

## Flags
- --unified-app-id <String>: 开放平台统一应用 ID
- --version-id <String>: 版本 ID
- --confirmed-sensitive <Bool>: 确认发布包含高敏权限的版本
- --approver-user-id <String>: 灰度选人模式下指定审批人 userId

## Related
- dws devapp +create
- dws devapp +credentials-get
- dws devapp +delete
- dws devapp +disable
- dws devapp +enable
- dws devapp +event-list
