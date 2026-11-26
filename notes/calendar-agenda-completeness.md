---
title: 个人日程汇总的范围、分页与来源
source_refs: skills/mono/references/best_practices/03-meeting.md, skills/mono/references/best_practices/lite-recipes.md, skills/mono/references/products/calendar.md, skills/mono/scripts/calendar_today_agenda.py, skills/multi/dingtalk-calendar/SKILL.md, skills/multi/dingtalk-calendar/references/03-meeting.md, skills/multi/dingtalk-calendar/references/calendar.md, skills/multi/dingtalk-calendar/references/lite-recipes.md, skills/multi/dingtalk-calendar/scripts/calendar_today_agenda.py, skills/multi/dingtalk-shared/references/recipes/lite-catalog.md
---

# 个人日程汇总的范围、分页与来源

## 先确认日历本范围

`calendar_today_agenda.py` 先执行一次 `dws calendar book list --format json`，从响应发现日历本。默认选择 `type=primary` 且 `privilege=owner` 的真实 `calendarId`，覆盖返回的本人钉钉和邮箱主日历。用户点名某本日历时，按明确指定且可读取的 ID 查询。只发现一本本人主日历时，说明本次覆盖范围。

产品说明 `calendar.md`、日历 `SKILL.md` 和 `lite-recipes.md` 共用这套选本规则。共享入口 `lite-catalog.md` 把查询交给日历 Skill，日历本发现由实际执行查询的流程完成。

{{code: skills/multi/dingtalk-calendar/scripts/calendar_today_agenda.py | def select_calendars}}

## 每本独立分页并核对完整性

`calendar_today_agenda.py` 使用相同的时间窗和 profile，逐本执行 `dws calendar event list --calendar-id <CALENDAR_ID>`。各本独立跟随游标，每本最多 20 页。查询或分页中断时，保留已有记录，结合 `calendars` 和 `failures` 说明哪些范围还没查完。`complete=true` 表示本次所列范围已取完。

{{code: skills/mono/scripts/calendar_today_agenda.py | MAX_PAGES = 20}}

## 汇总后保留原始日历来源

`calendar_today_agenda.py` 在同一本日历内按日程 ID、实例时间和全天属性去重。跨本合并用共同的 `iCalUid`，并要求实例时间和全天属性一致。合并记录保留各本的 `calendarId`、`eventId` 和状态。状态冲突时，汇总标为未知。

查详情或按 `03-meeting.md` 的流程改期时，带上对应来源的 `calendarId` 和 `eventId`，使后续操作落到同一本日历的正确实例。

{{code: skills/multi/dingtalk-calendar/scripts/calendar_today_agenda.py | target["sources"].append(source)}}
