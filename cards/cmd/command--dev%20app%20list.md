# dws dev app list

kind: command
completeness: partial
usage: dws dev app list
description: —
source: internal/helpers/devapp.go:416
visible_flags: 9
partial_reason: missing_description

## Flags
- --name <String>: 应用名称关键词
- --app-key <String>: 按 appKey/clientId 过滤
- --app-group-id <Int>: 应用分组 ID
- --creator <String>: 创建人名称关键词
- --robot-name <String>: 机器人名称关键词
- --develop-type <Int>: 开发类型枚举；不确定时不要传
- --filter-cool-app <Int>: 酷应用过滤枚举；不确定时不要传
- --sort-type <String>: 排序字段，如 gmt_modified
- … 1 more; use dwsdoc cmd/short for full flags

## Related
- dws dev app create
- dws dev app credentials
- dws dev app delete
- dws dev app disable
- dws dev app enable
- dws dev app event
