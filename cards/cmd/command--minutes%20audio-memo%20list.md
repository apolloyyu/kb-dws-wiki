# dws minutes audio-memo list

kind: command
completeness: full
usage: dws minutes audio-memo list
description: 查询语音备忘列表
example: dws minutes audio-memo list
source: internal/helpers/minutes.go:2079
visible_flags: 4

## Flags
- --max <Float64>: 每页数据条数 (默认 200，上限 1000)
- --cursor <Int64>: 翻页游标，回填上一页返回的 nextCursor (首页留空)
- --start <String>: 开始时间 ISO-8601 (可选，默认近一年)
- --end <String>: 结束时间 ISO-8601 (可选)

## Related
- none
