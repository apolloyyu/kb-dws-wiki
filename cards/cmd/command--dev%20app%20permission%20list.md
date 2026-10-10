# dws dev app permission list

kind: command
completeness: partial
usage: dws dev app permission list
description: —
source: internal/helpers/devapp.go:896
visible_flags: 6
partial_reason: missing_description

## Flags
- --unified-app-id <String> required: 开放平台统一应用 ID（必填）
- --keyword <String>: 权限名、权限点、接口名关键词
- --scope-value <String>: 精确权限点 scopeValue
- --auth-status <String>: 权限状态：ALL、AUTHED、UNAUTHED
- --scope-type <String>: 权限一级类型：APP 或 SNS
- --api-status <String>: 开发者后台 apiStatus 过滤

## Related
- dws dev app permission add
- dws dev app permission remove
