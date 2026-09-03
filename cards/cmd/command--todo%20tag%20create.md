# dws todo tag create

kind: command
completeness: full
usage: dws todo tag create
description: 创建待办标签
example: dws todo tag create --name "标签名"
source: internal/helpers/todo.go:1686
visible_flags: 1

## Flags
- --name <String>: 标签名称 (必填)

## Related
- dws todo tag add
- dws todo tag delete
- dws todo tag list
- dws todo tag update
