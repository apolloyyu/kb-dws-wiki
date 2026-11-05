# dws doc +update

kind: shortcut
completeness: partial
usage: dws doc +update
description: 追加、覆盖或按 block 精确更新文档内容
source: internal/shortcut/doc/content_shortcuts.go:429
visible_flags: 16
partial_reason: too_many_flags:16

## Flags
- --force <Bool>: 允许全文覆盖使本人待处理建议失效；独立于 --yes
- --suggestion <Bool>: —
- --src-block-ids <String>: 仅block_copy_insert_after可用的逗号分隔源ID；与block-id同时提供须相同
- --start-block-id <String>: block_delete/block_replace顶层范围起点；与end-block-id成对
- --end-block-id <String>: block_delete/block_replace顶层范围终点（含）；使用真实块 UUID
- --node <String>: 文档 ID 或 URL
- --command <String>: 更新动作；不能为空
- --content <String>: —
- … 8 more; use dwsdoc cmd/short for full flags

## Related
- dws doc +access-change
- dws doc +access-grant
- dws doc +access-revoke
- dws doc +background-delete
- dws doc +background-update
- dws doc +checkpoint-update
