# dws doc +version-revert

kind: shortcut
completeness: full
usage: dws doc +version-revert
description: 回滚文档到指定历史版本
source: internal/shortcut/doc/doc.go:810
visible_flags: 2

## Flags
- --node <String>: 文档 ID 或 URL
- --version <Int>: 目标版本号 (从 +version-list 获取)

## Related
- dws doc +background-delete
- dws doc +background-update
- dws doc +checkpoint-update
- dws doc +comment-create
- dws doc +comment-create-inline
- dws doc +comment-delete
