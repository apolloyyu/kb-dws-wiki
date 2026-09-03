# dws calendar attachment add

kind: command
completeness: full
usage: dws calendar attachment add
description: 添加日程附件
example: dws calendar attachment add --event EVENT_ID --files fileId1:report.pdf,fileId2:slides.pptx
source: internal/helpers/calendar.go:1274
visible_flags: 3

## Flags
- --event <String>: 日程 ID (必填)
- --files <String>: 附件列表，格式 <fileId>:<name>，多项逗号分隔 (必填)
- --calendar-id <String>: 日历 ID (可选，默认 primary 主日历；指定其他日历本时填写，可通过 book list 获取)。注意：订阅日历下的日程不支持添加附件

## Related
- none
