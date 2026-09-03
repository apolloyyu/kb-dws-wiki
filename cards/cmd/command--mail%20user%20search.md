# dws mail user search

kind: command
completeness: full
usage: dws mail user search
description: 搜索邮箱用户
example: dws mail user search --keyword "张三"
source: internal/helpers/mail.go:2614
visible_flags: 5

## Flags
- --email <String>: 搜索目标邮箱地址 (可选)
- --keyword <String>: 搜索关键词（未提供 --employee-no 时为必填）
- --employee-no <String>: 按工号搜索用户；提供此参数时 keyword 不再必填
- --cursor <String>: 分页游标，取自响应中的 nextCursor 字段
- --limit <String>: 每页返回数量

## Related
- none
