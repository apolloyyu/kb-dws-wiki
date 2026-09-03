# dws calendar acl delete

kind: command
completeness: full
usage: dws calendar acl delete
description: 删除日历访问权限
example: dws calendar acl delete --acl-id ACL_ID
source: internal/helpers/calendar.go:1430
visible_flags: 1

## Flags
- --acl-id <String>: 已授予权限的 ID (必填，可通过 acl list 查询)

## Related
- dws calendar acl add
- dws calendar acl list
