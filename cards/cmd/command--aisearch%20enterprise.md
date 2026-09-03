# dws aisearch enterprise

kind: command
completeness: full
usage: dws aisearch enterprise
description: 搜索企业内部知识内容和相关消息
example: dws aisearch enterprise --queries "智能化方案" --types document
source: internal/helpers/aisearch.go:311
visible_flags: 3

## Flags
- --queries <String>: 内容关键词列表，多个用逗号分隔；汇总类场景可留空
- --time-range <String>: 时间范围，仅当用户显式给出时间词时填写，如 今天/本周/9月/过去一周
- --types <String>: 搜索类型: all/document/im/calendar/todo/minute/report/image/link/notable/baike/mail，多个用逗号分隔

## Related
- dws aisearch behavior
- dws aisearch person
