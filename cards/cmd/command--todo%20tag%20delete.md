# dws todo tag delete

kind: command
completeness: full
usage: dws todo tag delete
description: 删除待办标签
example: dws todo tag delete --tag-codes code1,code2 --yes
source: internal/helpers/todo.go:1539
visible_flags: 1

## Flags
- --tag-codes <String>: 要删除的标签编码列表，逗号分隔 (必填)

## Related
- dws todo tag add
- dws todo tag create
- dws todo tag list
- dws todo tag update
