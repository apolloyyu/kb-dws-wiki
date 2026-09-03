# dws smart +detail

kind: shortcut
completeness: full
usage: dws smart +detail
description: 批量聚合听记基础信息、摘要、关键词、完整逐字稿和行动项，支持安全文件输出
source: internal/shortcut/smart/minutes_detail.go:55
visible_flags: 9

## Flags
- --id <String>: 单个听记 taskUuid
- --ids <StringSlice>: 多个听记 taskUuid，最多 50 个
- --artifacts <StringSlice>: 要拉取的产物子集（默认全部）
- --direction <String>: 逐字稿排序: 0=正序(默认), 1=倒序（可选）
- --cursor <String>: 逐字稿单页/续拉的起始 nextToken
- --single-page <Bool>: 逐字稿只读取一页并返回 nextToken
- --page-limit <Int>: —
- --transcript-output <String>: —
- --output-dir <String>: —

## Related
- dws smart +access-change
- dws smart +access-grant
- dws smart +access-revoke
- dws smart +action-items
- dws smart +assign
- dws smart +assign-multi
