# dws oa approval list-initiated

kind: command
completeness: full
description: List approval instances the current user has initiated under a specified approval template (processCode).
use_when: When the agent reviews the status of approvals the user submitted.
source: internal/helpers/oa.go:1240
visible_flags: 7

## Flags
- --process-code <String>: 表单 processCode (必填)
- --start <String>: 开始时间 ISO-8601 (如 2026-03-10T00:00:00+08:00)，与 end 间隔不超过120天 (必填)
- --end <String>: 结束时间 ISO-8601 (如 2026-03-10T23:59:59+08:00)，与 start 间隔不超过120天 (必填)
- --cursor <String>: 分页游标，首次传 0
- --next-token <String>: 分页游标，首次传 0
- --limit <String>: 每页大小，最大 20
- --max-results <String>: 每页大小，最大 20

## Related
- dws oa approval approve
- dws oa approval create-instance
- dws oa approval detail
- dws oa approval forecast-process
- dws oa approval form-schema
- dws oa approval list-by-admin
