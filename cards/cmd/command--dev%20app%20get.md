# dws dev app get

kind: command
completeness: partial
usage: dws dev app get
description: —
source: internal/helpers/devapp.go:462
visible_flags: 2
partial_reason: missing_description

## Flags
- --unified-app-id <String>: 开放平台统一应用 ID（与 --app-key 二选一）
- --app-key <String>: 按 appKey/clientId 查询应用详情（与 --unified-app-id 二选一）

## Related
- dws dev app create
- dws dev app credentials
- dws dev app delete
- dws dev app disable
- dws dev app enable
- dws dev app event
