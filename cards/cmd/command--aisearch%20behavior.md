# dws aisearch behavior

kind: command
completeness: full
usage: dws aisearch behavior
description: 搜索明确的发送/创建/接收等行为记录
example: dws aisearch behavior --types mail --behavior-type send --direction "我->汐峰"
source: internal/helpers/aisearch.go:385
visible_flags: 6

## Flags
- --queries <String>: 内容关键词列表，多个用逗号分隔；汇总类场景可留空
- --types <String>: 搜索类型: all/document/im/calendar/todo/minute/report/image/link/notable/baike/mail，多个用逗号分隔
- --chat-scope <String>: 消息所在会话/群范围，仅 IM 类型且用户明确指定群名时填写
- --behavior-type <String>: 行为类型: all/send/create/share/edit/receive
- --time-range <String>: 时间范围，仅当用户显式给出时间词时填写，如 今天/本周/9月/过去一周
- --direction <String>: 我<->汐峰

## Related
- dws aisearch enterprise
- dws aisearch person
