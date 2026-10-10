# dws dev app version create

kind: command
completeness: partial
usage: dws dev app version create
description: —
source: internal/helpers/devapp.go:1539
visible_flags: 3
partial_reason: missing_description

## Flags
- --unified-app-id <String> required: 开放平台统一应用 ID（必填）
- --version <String>: 高级可选：显式版本号，如 1.0.1；默认不传，由服务端基于最新已发布版本自动递增
- --desc <String>: 版本描述

## Related
- dws dev app version check-approval
- dws dev app version get
- dws dev app version list
- dws dev app version publish
- dws dev app version status
