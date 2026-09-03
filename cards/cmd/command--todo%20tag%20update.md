# dws todo tag update

kind: command
completeness: full
usage: dws todo tag update
description: 更新待办标签
example: dws todo tag update --user-tags '[{"code":"code1","name":"新名称"}]'
source: internal/helpers/todo.go:1591
visible_flags: 1

## Flags
- --user-tags <String>: 标签列表 JSON 数组 (必填)

## Related
- dws todo tag add
- dws todo tag create
- dws todo tag delete
- dws todo tag list
