# dws chat bot find

kind: command
completeness: full
usage: dws chat bot find
description: 搜索【全部可用】机器人（含他人/官方，额外返回 openDingTalkId 可发单聊）
example: dws chat bot find --query "日报"
source: internal/helpers/chat.go:8900
visible_flags: 3

## Flags
- --query <String>: 搜索关键词 (必填)
- --limit <Int>: 每页返回数量（默认 20）
- --cursor <String>: 分页游标（首次调用不传，翻页时传上次返回的 nextCursor）

## Related
- dws chat bot search
