# dws doc +search

kind: shortcut
completeness: partial
usage: dws doc +search
description: 按关键词或过滤条件搜索有权限的文档；默认只读取一页
source: internal/shortcut/doc/doc.go:38
visible_flags: 21
partial_reason: too_many_flags:21

## Flags
- --folder <String>: 在搜索条件外限制文档文件夹直接成员（不递归）；要求page-all，两组分页分别读取完整搜索候选与目录；仅列目录用doc +list
- --query <String>: 搜索关键词；不传仍兼容返回默认结果页，最近访问/编辑应使用 drive +recent
- --extensions <StringSlice>: 按文件扩展名过滤 (如 adoc,axls,pdf)
- --created-after <String>: 创建起点：RFC3339带时区或YYYY-MM-DD（UTC）；与created-from互斥
- --created-before <String>: 创建终点：RFC3339带时区或YYYY-MM-DD（UTC）；与created-to互斥
- --visited-after <String>: 访问起点：RFC3339带时区或YYYY-MM-DD（UTC）；与visited-from互斥
- --visited-before <String>: 访问终点：RFC3339带时区或YYYY-MM-DD（UTC）；与visited-to互斥
- --with-metadata <Bool>: 在每条结果metadata中保留下游原始字段；不改变默认精简结果
- … 13 more; use dwsdoc cmd/short for full flags

## Related
- dws doc +background-delete
- dws doc +background-update
- dws doc +checkpoint-update
- dws doc +comment-create
- dws doc +comment-create-inline
- dws doc +comment-delete
