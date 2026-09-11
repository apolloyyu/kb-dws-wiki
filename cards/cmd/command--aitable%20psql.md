# dws aitable psql

kind: command
completeness: full
usage: dws aitable psql
description: 以 PostgreSQL 逻辑表方式查询 AI 表格
source: internal/helpers/aitable_psql.go:24
visible_flags: 8

## Flags
- --database (-d) <String>: AI 表格 Base ID（必填）
- --list (-l) <Bool>: 列出 Base 内可查询的逻辑表
- --table (-t) <String>: 查看表结构时使用的 tableId
- --all-properties <Bool>: 查看表结构时展开字段的全部属性列
- --expanded (-x) <Bool>: 按 psql expanded display 逐行纵向展示查询结果
- --command (-c) <String>: 执行一条标准 PostgreSQL SELECT
- --limit <Int>: 最大返回行数，范围 1-1000
- --timeout <Int>: 查询超时秒数，范围 1-60

## Related
- dws aitable advperm
- dws aitable app
- dws aitable attachment
- dws aitable base
- dws aitable chart
- dws aitable comment
