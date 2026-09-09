# dws drive recent

kind: command
completeness: full
usage: dws drive recent
description: 获取最近访问/编辑的文档列表
example: dws drive recent
source: internal/helpers/drive.go:3710
visible_flags: 3

## Flags
- --creator-type <Int>: 按创建人过滤: 0=全部, 1=我创建, 2=他人创建
- --limit <Int>: 每页数量 (默认 20，最大 20)
- --cursor <String>: 分页游标 (从上次结果的 nextCursor 获取)

## Related
- dws drive comment
- dws drive commit
- dws drive copy
- dws drive cover
- dws drive delete
- dws drive download
