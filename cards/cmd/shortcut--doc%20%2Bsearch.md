# dws doc +search

kind: shortcut
completeness: partial
usage: dws doc +search
description: 按关键词或过滤条件搜索有权限的文档；默认只读取一页
source: internal/shortcut/doc/doc.go:38
visible_flags: 15
partial_reason: too_many_flags:15

## Flags
- --query <String>: 搜索关键词；不传仍兼容返回默认结果页，最近访问/编辑应使用 drive +recent
- --extensions <StringSlice>: 按文件扩展名过滤 (如 adoc,axls,pdf)
- --created-from <Int>: 创建时间起始 (毫秒时间戳)
- --created-to <Int>: 创建时间截止 (毫秒时间戳)
- --visited-from <Int>: 访问时间起始 (毫秒时间戳)
- --visited-to <Int>: 访问时间截止 (毫秒时间戳)
- --creator-uids <StringSlice>: 按创建者用户 ID 过滤
- --editor-uids <StringSlice>: 按编辑者用户 ID 过滤
- … 7 more; use dwsdoc cmd/short for full flags

## Related
- dws doc +background-delete
- dws doc +background-update
- dws doc +checkpoint-update
- dws doc +comment-create
- dws doc +comment-create-inline
- dws doc +comment-delete
