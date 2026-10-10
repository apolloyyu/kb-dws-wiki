# dws dev app version publish

kind: command
completeness: partial
usage: dws dev app version publish
description: —
source: internal/helpers/devapp.go:1677
visible_flags: 4
partial_reason: missing_description

## Flags
- --unified-app-id <String> required: 开放平台统一应用 ID（必填）
- --version-id <String> required: 版本 ID (必填)
- --approver-user-id <String>: 灰度选人模式下指定审批人 userId
- --confirmed-sensitive <Bool>: 确认发布包含高敏权限的版本

## Related
- dws dev app version check-approval
- dws dev app version create
- dws dev app version get
- dws dev app version list
- dws dev app version status
