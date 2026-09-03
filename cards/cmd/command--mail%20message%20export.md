# dws mail message export

kind: command
completeness: full
usage: dws mail message export
description: 导出/备份邮件（EML格式）
example: dws mail message export --email user@company.com --id <messageId>
source: internal/helpers/mail.go:2201
visible_flags: 4

## Flags
- --email <String>: 用户的邮箱地址 (必填)
- --id <String>: 邮件ID (必填)
- --filename <String>: 导出文件名（不含扩展名），默认使用邮件主题
- --overwrite <Bool>: 是否覆盖同名文件，默认 false

## Related
- dws mail message batch-delete
- dws mail message batch-get
- dws mail message batch-move
- dws mail message batch-update
- dws mail message forward
- dws mail message get
