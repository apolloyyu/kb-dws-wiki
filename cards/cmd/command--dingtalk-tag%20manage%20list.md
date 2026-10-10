# dws dingtalk-tag manage list

kind: command
completeness: partial
usage: dws dingtalk-tag manage list
description: —
source: internal/helpers/deap_agent.go:341
visible_flags: 4
partial_reason: missing_description

## Flags
- --keyword <String>: 按名称或职责等可见信息模糊匹配
- --type <String>: 按主程序类型筛选：open_code 或 local_agent；对应 MCP 字段 type，不传表示不过滤
- --page <Int>: 页码
- --page-size <Int>: 每页数量

## Related
- dws dingtalk-tag manage create
- dws dingtalk-tag manage delete
- dws dingtalk-tag manage detail
- dws dingtalk-tag manage login
- dws dingtalk-tag manage publish
- dws dingtalk-tag manage save-draft
