# dws mail thread list

kind: command
completeness: full
usage: dws mail thread list
description: 列出邮件会话
example: dws mail thread list --email user@company.com --folder <folderId> --limit 10
source: internal/helpers/mail.go:1006
visible_flags: 7

## Flags
- --email <String>: 会话所属邮箱地址 (必填)
- --folder <String>: 邮件文件夹 ID，不是文件夹名称 (必填)
- --limit <Int>: 本次列出的会话数，最大 100 (必填)
- --cursor <String>: 分页游标，首次请求可不传 (可选)
- --start <String>: 开始 UTC 时间字符串，如 2024-01-01T00:00:00Z (可选)
- --end <String>: 结束 UTC 时间字符串，如 2024-12-31T23:59:59Z (可选)
- --ascending <Bool>: 是否按时间升序；不传由服务端默认排序 (可选)

## Related
- dws mail thread batch-trash
- dws mail thread batch-update
- dws mail thread get
- dws mail thread trash
- dws mail thread update
