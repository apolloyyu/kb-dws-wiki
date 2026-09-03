# dws devapp +version-check-approval

kind: shortcut
completeness: full
description: 预检版本发布是否需要审批（不实际发布）
source: internal/shortcut/devapp/devapp.go:2415
visible_flags: 2

## Flags
- --unified-app-id <String>: 开放平台统一应用 ID
- --version-id <String>: 版本 ID

## Related
- dws devapp +create
- dws devapp +credentials-get
- dws devapp +delete
- dws devapp +disable
- dws devapp +enable
- dws devapp +event-list
