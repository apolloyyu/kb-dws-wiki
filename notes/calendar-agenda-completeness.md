---
title: 个人日程汇总的范围、分页与来源
source_refs: skills/mono/references/best_practices/03-meeting.md, skills/mono/references/best_practices/lite-recipes.md, skills/mono/references/products/calendar.md, skills/mono/scripts/calendar_today_agenda.py, skills/multi/dingtalk-calendar/SKILL.md, skills/multi/dingtalk-calendar/references/03-meeting.md, skills/multi/dingtalk-calendar/references/calendar.md, skills/multi/dingtalk-calendar/references/lite-recipes.md, skills/multi/dingtalk-calendar/scripts/calendar_today_agenda.py, skills/multi/dingtalk-shared/references/recipes/lite-catalog.md
---

# 个人日程汇总的范围、分页与来源

## 先确认日历本范围

`calendar_today_agenda.py` 先执行一次 `dws calendar book list --format json`。默认按真实 `calendarId` 选择 `privilege=owner` 且 `type` 为 `primary` 或 `shared` 的本人日历。邮箱日历可能返回 `type=shared`，需要结合 `privilege` 判断归属。订阅、团队、公共日历和仅有 `reader` 或 `writer` 权限的日历默认排除。用户点名某本日历时，可用 `--calendar-id` 指定发现结果中可读取的 ID，该参数可重复。只发现一本本人日历时，应说明本次覆盖范围。

产品说明 `calendar.md`、日历 `SKILL.md` 和 `lite-recipes.md` 共用这套选本规则。共享入口 `lite-catalog.md` 把查询交给日历 Skill，日历本发现由实际执行查询的流程完成。

{{code: skills/multi/dingtalk-calendar/scripts/calendar_today_agenda.py | def select_calendars}}

## 每本独立分页并核对完整性

`calendar_today_agenda.py` 使用相同的时间窗和 profile，逐本执行 `dws calendar event list --calendar-id <CALENDAR_ID>`。预设 `today`、`yesterday`、`tomorrow` 和 `week` 按北京时间计算。自定义时间窗用成对且带时区的 `--start`、`--end`，与日期预设互斥。

各本独立跟随 `nextCursor`，直到 `hasMore=false` 且游标为空，每本最多 20 页。查询失败、游标矛盾或重复时保留已有记录。JSON 的 `calendars` 和 `failures` 说明哪些范围还没查完，退出码 `1` 仍可能带有部分结果。`complete=true` 只表示所列日历在本次时间窗内已取完。

{{code: skills/mono/scripts/calendar_today_agenda.py | MAX_PAGES = 20}}

## 汇总后保留原始日历来源

`calendar_today_agenda.py` 在同一本日历内按日程 ID、实例时间和全天属性去重。跨本合并用共同的 `iCalUid`，并要求实例时间和全天属性一致。合并记录保留各本的 `calendarId`、`eventId` 和状态。状态冲突时，汇总标为未知。

查详情或参会人时，使用 `sources` 中对应的日程 ID，并通过 `--calendar-id` 带上该来源日历。按 `03-meeting.md` 的流程改期时也沿用这组 ID，使操作落到同一本日历的正确实例。

{{code: skills/multi/dingtalk-calendar/scripts/calendar_today_agenda.py | target["sources"].append(source)}}
