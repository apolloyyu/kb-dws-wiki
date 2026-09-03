# dws mail attachment download

kind: command
completeness: full
usage: dws mail attachment download
description: 下载邮件附件到本地
example: dws mail attachment download --email user@company.com --message-id <messageId> --attachment-id <attachmentId> --name report.pdf
source: internal/helpers/mail.go:2045
visible_flags: 5

## Flags
- --email <String>: 用户邮箱地址 (必填)
- --message-id <String>: 邮件唯一标识 messageId (必填)
- --attachment-id <String>: 附件唯一标识，取自 attachment list 的 id 字段 (必填)
- --name <String>: 保存到本地的文件名，取自 attachment list 的 name 字段 (必填)
- --output <String>: 保存目录，默认为当前目录

## Related
- dws mail attachment list
