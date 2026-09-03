# dws report list

kind: command
completeness: full
usage: dws report list
description: List reports the current user has received from others.
example: dws report list --start "2026-03-10T00:00:00+08:00" --end "2026-03-10T23:59:59+08:00" --cursor 0 --size 20
use_when: When the agent digests the user's incoming reports (e.g. team members' weeklies).
source: internal/helpers/report.go:483
visible_flags: 5

## Flags
- --start <String>: 开始时间 ISO-8601 (如 2026-03-10T00:00:00+08:00) (必填)
- --end <String>: 结束时间 ISO-8601 (如 2026-03-10T23:59:59+08:00) (必填)
- --cursor <Int>: 分页游标（默认 0，翻页传返回的 cursor）
- --size <Int>: 每页条数（默认 20，最大 20）
- --sender-user-ids <StringSlice>: 发送人 staffId 列表，逗号分隔，用于过滤指定发送人的日志

## Related
- dws report create
- dws report created
- dws report detail
- dws report entry
- dws report inbox
- dws report outbox
