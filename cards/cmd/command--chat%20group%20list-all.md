# dws chat group list-all

kind: command
completeness: full
description: 拉取指定时间范围内当前用户的所有会话消息
source: internal/helpers/chat.go:4305
visible_flags: 4

## Flags
- --start <String>: 起始时间，格式: yyyy-MM-dd HH:mm:ss（可选，默认当前时间前 1 天）
- --end <String>: 结束时间，格式: yyyy-MM-dd HH:mm:ss（可选，默认当前时间）
- --limit <Int>: 每页返回数量（默认 50）
- --cursor <String>: 分页游标（首页传 \"0\"，后续从响应中获取）

## Related
- dws chat group audit-join-validation
- dws chat group bots
- dws chat group create
- dws chat group dismiss
- dws chat group get-by-group-id
- dws chat group get-mute-config
