# dws smart +transcript

kind: shortcut
completeness: full
usage: dws smart +transcript
description: 读取指定或我最新一条听记的完整逐字稿，并交付分页完整性证据
source: internal/shortcut/smart/transcript.go:45
visible_flags: 6

## Flags
- --id <String>: 听记 taskUuid；不传时选择我最新的一条
- --keyword <String>: 按关键字过滤听记（可选）
- --direction <String>: 排序方向: 0=正序(默认), 1=倒序（可选）
- --cursor <String>: 单页/续拉的起始 nextToken
- --single-page <Bool>: 只读取一页；输出 data.complete 与 meta.pagination.next_token
- --page-limit <Int>: —

## Related
- dws smart +access-change
- dws smart +access-grant
- dws smart +access-revoke
- dws smart +action-items
- dws smart +assign
- dws smart +assign-multi
