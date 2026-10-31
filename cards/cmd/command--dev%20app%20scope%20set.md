# dws dev app scope set

kind: command
completeness: partial
usage: dws dev app scope set
description: —
source: internal/helpers/devapp.go:734
visible_flags: 8
partial_reason: missing_description

## Flags
- --unified-app-id <String> required: 开放平台统一应用 ID（必填）
- --dept-visible-scopes <String>: 可见部门 ID，CSV 或 JSON 数组
- --user-visible-scopes <String>: 可见用户 ID，CSV 或 JSON 数组；scope set 为全量替换语义，未传入的既有范围会被移除
- --role-visible-scopes <String>: 可见角色 ID，CSV 或 JSON 数组
- --dynamic-group-scopes <String>: 可见动态组编码，CSV 或 JSON 数组
- --is-hidden <Bool>: 是否隐藏应用
- --precheck-only <Bool>: 只生成计划，不创建版本或发布
- --publish <Bool>: 创建版本后是否立即发布；显式传 false 可仅创建版本

## Related
- dws dev app scope get
