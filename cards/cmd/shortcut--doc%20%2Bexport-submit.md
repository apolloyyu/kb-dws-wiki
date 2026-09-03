# dws doc +export-submit

kind: shortcut
completeness: full
description: 提交在线文档导出任务 (docx/markdown/pdf)，返回 jobId
source: internal/shortcut/doc/doc.go:621
visible_flags: 2

## Flags
- --node <String>: 要导出的文档 ID 或 URL
- --export-format <String>: —

## Related
- dws doc +background-delete
- dws doc +background-update
- dws doc +checkpoint-update
- dws doc +comment-create
- dws doc +comment-create-inline
- dws doc +comment-delete
