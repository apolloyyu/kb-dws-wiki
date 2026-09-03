# dws doc version list

kind: command
completeness: full
usage: dws doc version list
description: 查看文档历史版本列表
example: dws doc version list --node DOC_ID
source: internal/helpers/doc.go:4450
visible_flags: 3

## Flags
- --node <String>: 文档 ID 或 URL (必填)
- --limit <Int>: 返回版本数量上限
- --cursor <String>: 分页游标

## Related
- dws doc version revert
- dws doc version save
