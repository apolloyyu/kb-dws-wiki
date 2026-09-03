# dws calendar room search

kind: command
completeness: full
usage: dws calendar room search
description: Search meeting rooms by keyword within a group, optionally filtering to rooms free during a given window via `--available`.
example: dws calendar room search --room-name 永澄亭
use_when: When the agent needs to find a suitable room, typically free at a specific time, prior to booking.
source: internal/helpers/calendar.go:838
visible_flags: 6

## Flags
- --start <String>: 开始时间 ISO-8601 (可选，不传则默认当前时间+1分钟，例如 2026-03-10T14:00:00+08:00)
- --end <String>: 结束时间 ISO-8601 (可选，不传则默认当前时间+1小时，例如 2026-03-10T15:00:00+08:00)
- --group-id <String>: 会议室分组ID（可选，留空查根目录；会议室超100条时先用 list-groups 获取分组再按分组查询）
- --room-name <String>: 按会议室名称过滤（可选，服务端模糊匹配。调用方需先剔除用户口语后缀如「会议室/大会议室/小会议室」，仅传核心专名以提升命中率，例如用户说「永澄亭会议室」应传「永澄亭」）
- --limit <String>: 页大小 (可选，不填默认 100，超过 100 按 100 处理)
- --page <String>: 分页起始位置 (可选，不填默认 0)

## Related
- dws calendar room add
- dws calendar room delete
- dws calendar room list-groups
