# dws doc +version-list

kind: shortcut
completeness: full
usage: dws doc +version-list
description: 查看文档历史版本列表
source: internal/shortcut/doc/doc.go:760
visible_flags: 3

## Flags
- --node <String>: 文档 ID 或 URL
- --limit <Int>: 返回版本数量上限
- --cursor <String>: 分页游标

## Related
- dws doc +background-delete
- dws doc +background-update
- dws doc +checkpoint-update
- dws doc +comment-create
- dws doc +comment-create-inline
- dws doc +comment-delete
