# dws todo comment list

kind: command
completeness: full
description: 查询待办列表
source: internal/helpers/todo.go:277
visible_flags: 8

## Flags
- --page <String>: 页码（默认 1）
- --size <String>: 获取数量，超过 20 自动分页 (默认 20)
- --status <String>: true=已完成, false=未完成
- --priority <String>: 优先级: 10 低/20 普通/30 较高/40 紧急
- --role-types <String>: 角色类型: creator/executor/participant
- --plan-finish-date-start <String>: 截止时间范围查询开始 ISO-8601 (如 2026-03-10T18:00:00+08:00)
- --plan-finish-date-end <String>: 截止时间范围查询结束 ISO-8601 (如 2026-03-10T18:00:00+08:00)
- --query-all <Bool>: 查询所有待办，而不是仅查询当前组织待办

## Related
- dws todo comment add
- dws todo comment delete
