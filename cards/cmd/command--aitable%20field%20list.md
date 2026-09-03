# dws aitable field list

kind: command
completeness: full
description: 获取 AI 表格列表
source: internal/helpers/aitable.go:1722
visible_flags: 2

## Flags
- --limit <Int>: 每页数量，默认 10，最大 10
- --cursor <String>: 首次不传；传入上次返回的游标继续获取下一页

## Related
- dws aitable field create
- dws aitable field delete
- dws aitable field get
- dws aitable field search-options
- dws aitable field update
