# dws mail auto-reply update

kind: command
completeness: full
usage: dws mail auto-reply update
description: 更新/设置用户的自动回复配置
example: dws mail auto-reply update --email user@company.com --enabled true --start "2026/07/01 09:00:00 +0800" --end "2026/07/07 18:00:00 +0800" --scope all --content "出差中，请稍后联系"
source: internal/helpers/mail.go:3351
visible_flags: 6

## Flags
- --email <String>: 用户的邮箱地址 (必填)
- --enabled <String>: 是否启用自动回复: true/false (必填)
- --start <String>: 自动回复开始时间，格式: YYYY/MM/DD HH:MM:SS +ZZZZ (必填)
- --end <String>: 自动回复结束时间，格式: YYYY/MM/DD HH:MM:SS +ZZZZ (必填)
- --scope <String>: 回复范围: contact(仅联系人)/all(所有人) (必填)
- --content <String>: 自动回复内容 (必填)

## Related
- dws mail auto-reply get
