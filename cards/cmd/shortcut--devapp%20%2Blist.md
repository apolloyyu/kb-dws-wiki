# dws devapp +list

kind: shortcut
completeness: full
usage: dws devapp +list
description: 查询开放平台企业内部应用列表
source: internal/shortcut/devapp/devapp.go:424
visible_flags: 9

## Flags
- --name <String>: 应用名称关键词
- --app-key <String>: 按 appKey/clientId 过滤
- --app-group-id <Int>: 应用分组 ID
- --creator <String>: 创建人名称关键词
- --robot-name <String>: 机器人名称关键词
- --develop-type <Int>: 开发类型枚举；不确定时不要传
- --filter-cool-app <Int>: 酷应用过滤枚举；不确定时不要传
- --sort-type <String>: 排序字段，如 gmt_modified
- --sort-order <String>: 排序方向 asc 或 desc

## Related
- dws devapp +create
- dws devapp +credentials-get
- dws devapp +delete
- dws devapp +disable
- dws devapp +enable
- dws devapp +event-list
