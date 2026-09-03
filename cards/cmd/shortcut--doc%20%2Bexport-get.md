# dws doc +export-get

kind: shortcut
completeness: full
usage: dws doc +export-get
description: 根据 jobId 查询文档导出任务结果
source: internal/shortcut/doc/doc.go:670
visible_flags: 1

## Flags
- --job-id <String>: 导出任务 ID

## Related
- dws doc +background-delete
- dws doc +background-update
- dws doc +checkpoint-update
- dws doc +comment-create
- dws doc +comment-create-inline
- dws doc +comment-delete
