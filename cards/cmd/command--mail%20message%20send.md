# dws mail message send

kind: command
completeness: full
usage: dws mail message send
description: 发送邮件
example: dws mail message send --from user@company.com
source: internal/helpers/mail.go:501
visible_flags: 7

## Flags
- --from <String>: 发件人邮箱 (必填)
- --to <String>: 收件人列表 (必填)
- --subject <String>: 邮件标题 (必填)
- --content <String>: 邮件正文 (必填)
- --cc <String>: 抄送人列表
- --attachment <StringArray>: 附件文件路径，可多次指定 (可选)
- --inline-attachment <StringArray>: 内联附件文件路径（如图片），可多次指定，cid 自动生成 (可选)

## Related
- dws mail message batch-delete
- dws mail message batch-get
- dws mail message batch-move
- dws mail message batch-update
- dws mail message export
- dws mail message forward
