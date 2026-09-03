# dws mail +thread-list

kind: shortcut
completeness: full
usage: dws mail +thread-list
description: 列出指定邮箱文件夹下的邮件会话（thread）
source: internal/shortcut/mail/mail.go:52
visible_flags: 7

## Flags
- --email <String>: 会话所属邮箱地址
- --folder <String>: 邮件文件夹 ID（不是文件夹名称）
- --limit <Int>: —
- --cursor <String>: 分页游标，首次请求可不传
- --start <String>: 开始 UTC 时间，如 2024-01-01T00:00:00Z
- --end <String>: 结束 UTC 时间，如 2024-12-31T23:59:59Z
- --ascending <Bool>: 是否按时间升序

## Related
- dws mail +contact-list
- dws mail +draft-create
- dws mail +draft-edit
- dws mail +folder-list
- dws mail +message
- dws mail +messages
