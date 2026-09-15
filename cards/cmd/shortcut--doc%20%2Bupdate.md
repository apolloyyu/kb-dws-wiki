# dws doc +update

kind: shortcut
completeness: full
usage: dws doc +update
description: 追加、覆盖或按 block 精确更新文档内容
source: internal/shortcut/doc/content_shortcuts.go:426
visible_flags: 14

## Flags
- --src-block-ids <String>: 仅block_copy_insert_after可用的逗号分隔源ID；与block-id同时提供须相同
- --start-block-id <String>: block_delete/block_replace顶层范围起点；与end-block-id成对，0表示第一块
- --end-block-id <String>: block_delete/block_replace顶层范围终点（含），-1表示最后块；最多50块
- --node <String>: 文档 ID 或 URL
- --command <String>: 更新动作；不能为空
- --content <String>: —
- --doc-format <String>: —
- --block-id <String>: 目标或源 block ID；相关动作要求时不能为空；block_delete 支持逗号分隔批量 ID，单次最多 50 个；block_copy_insert_after支持同文档顶层有序多源ID，最多20个，不支持含资源引用的块
- --after-block-id <String>: 插入位置参考 block ID；相关动作要求时不能为空
- --before-block-id <String>: 向前插入时的位置参考 block ID；block_insert_before 要求不能为空
- --heading-level <Int>: 将插入内容写为指定级别标题（1-6）；仅支持 Markdown block_insert_before/block_insert_after
- --old <String>: str_replace 原文字，不能为空
- --new <String>: str_replace 新文字；--old 不能为空，新值可为空但参数必须显式提供
- --expected-revision <Int>: 仅 overwrite+jsonml：传给服务端执行原子 revision 条件写

## Related
- dws doc +background-delete
- dws doc +background-update
- dws doc +checkpoint-update
- dws doc +comment-create
- dws doc +comment-create-inline
- dws doc +comment-delete
