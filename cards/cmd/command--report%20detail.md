# dws report detail

kind: command
completeness: full
usage: dws report detail
description: Retrieve the full details of a specific report entry, including fields and recipients.
example: dws report detail --report-id <reportId>
use_when: When the agent needs to read a report's content for summarization or follow-up.
source: internal/helpers/report.go:475
visible_flags: 1

## Flags
- --report-id <String>: 日志 ID (必填)

## Related
- dws report create
- dws report created
- dws report entry
- dws report inbox
- dws report list
- dws report outbox
