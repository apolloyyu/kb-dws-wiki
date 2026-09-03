# dws mail message reply-all

kind: command
completeness: full
description: 回复所有人
source: internal/helpers/mail.go:1434
visible_flags: 7

## Flags
- --from <String>: 发件人邮箱 (必填)
- --to <String>: 收件人列表
- --id <String>: 要回复的邮件 ID (必填)
- --subject <String>: 回复邮件标题
- --content <String>: 回复正文
- --attachment <StringArray>: 附件文件路径，可多次指定 (可选)
- --inline-attachment <StringArray>: 内联附件文件路径（如图片），可多次指定，cid 自动生成 (可选)

## Related
- dws mail message batch-delete
- dws mail message batch-move
- dws mail message export
- dws mail message forward
- dws mail message get
- dws mail message list
