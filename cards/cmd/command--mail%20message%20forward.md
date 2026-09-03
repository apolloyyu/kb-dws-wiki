# dws mail message forward

kind: command
completeness: full
description: 转发邮件
source: internal/helpers/mail.go:1515
visible_flags: 7

## Flags
- --from <String>: 发件人邮箱 (必填)
- --to <String>: 转发收件人列表
- --id <String>: 要转发的邮件 ID (必填)
- --subject <String>: 转发邮件标题
- --content <String>: 转发附言
- --attachment <StringArray>: 附件文件路径，可多次指定 (可选)
- --inline-attachment <StringArray>: 内联附件文件路径（如图片），可多次指定，cid 自动生成 (可选)

## Related
- dws mail message batch-delete
- dws mail message batch-move
- dws mail message export
- dws mail message get
- dws mail message list
- dws mail message reply
