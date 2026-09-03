# dws calendar acl add

kind: command
completeness: full
usage: dws calendar acl add
description: 把我的日历共享给某人
example: dws calendar acl add --user USER_ID --privilege reader
source: internal/helpers/calendar.go:1396
visible_flags: 3

## Flags
- --user <String>: 授予权限的目标用户 ID (必填)
- --privilege <String>: 授予的日历权限 (必填): free_busy_reader|title_reader|reader|writer
- --no-notification <Bool>: 不向被授权用户发送提醒 (默认发送)

## Related
- dws calendar acl delete
- dws calendar acl list
