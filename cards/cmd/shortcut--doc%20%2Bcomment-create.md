# dws doc +comment-create

kind: shortcut
completeness: full
description: 创建全文评论，或按 selection 创建划词评论
source: internal/shortcut/doc/doc.go:493
visible_flags: 8

## Flags
- --node <String>: 文档 ID 或 URL
- --content <String>: 评论文字内容
- --selection <String>: 完整文字或 前缀...后缀；
- --block-id <String>: 高级通道 block ID；
- --start <Int>: 块内 UTF-16 起始偏移；
- --end <Int>: 块内 UTF-16 结束偏移；
- --selected-text <String>: 可选引用原文；CLI 会从 block 回读并交叉校验
- --mention <StringSlice>: 被 @ 的用户 uid，多个值用逗号分隔；不要传 JSON 数组

## Related
- dws doc +background-delete
- dws doc +background-update
- dws doc +checkpoint-update
- dws doc +comment-create-inline
- dws doc +comment-delete
- dws doc +comment-list
