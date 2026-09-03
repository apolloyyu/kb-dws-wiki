# dws mail message search

kind: command
completeness: full
usage: dws mail message search
description: 搜索邮件 (KQL 语法)
example: dws mail message search --email user@company.com --query "subject:\"周报\"" --limit 20
source: internal/helpers/mail.go:274
visible_flags: 4

## Flags
- --email <String>: 搜索目标邮箱地址 (必填)
- --query <String>: KQL 查询表达式 (必填), 其中 date 格式必须遵循 ISO8601 规范
- --limit <String>: 每页返回数量(最大限制 100, 默认 20)
- --cursor <String>: 邮件的起始偏移标识, 其值取自响应中的nextCursor字段。\"\"表示从头开始

## Related
- dws mail message batch-delete
- dws mail message batch-get
- dws mail message batch-move
- dws mail message batch-update
- dws mail message export
- dws mail message forward
