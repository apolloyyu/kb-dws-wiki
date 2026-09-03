# dws doc +update

kind: shortcut
completeness: full
description: 追加、覆盖或按 block 精确更新文档内容
source: internal/shortcut/doc/content_shortcuts.go:377
visible_flags: 11

## Flags
- --node <String>: 文档 ID 或 URL
- --command <String>: 更新动作；不能为空
- --content <String>: —
- --doc-format <String>: —
- --block-id <String>: 目标或源 block ID；相关动作要求时不能为空
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
