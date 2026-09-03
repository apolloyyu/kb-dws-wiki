# dws doc +comment-create-inline

kind: shortcut
completeness: full
usage: dws doc +comment-create-inline
description: 兼容入口：按 block/start/end 创建划词评论
source: internal/shortcut/doc/doc.go:594
visible_flags: 7

## Flags
- --node <String>: 文档 ID 或 URL
- --content <String>: 评论文字内容 (纯文本)
- --block-id <String>: 评论标记所在的块 ID (通过 +block-list 获取)
- --start <Int>: 块内文本起始字符偏移量 (从 0 开始)
- --end <Int>: 块内文本结束字符偏移量 (须大于 start)
- --selected-text <String>: 选中文本内容 (展示引用原文)
- --mention <StringSlice>: 被 @ 的用户 uid，多个值用逗号分隔；不要传 JSON 数组

## Related
- dws doc +background-delete
- dws doc +background-update
- dws doc +checkpoint-update
- dws doc +comment-create
- dws doc +comment-delete
- dws doc +comment-list
