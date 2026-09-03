# dws aitable import data

kind: command
completeness: full
description: Import previously-uploaded data (e.g. Excel) into a datasheet as records, optionally creating fields.
use_when: When the agent is bulk-loading external data into a Base after a successful import upload.
source: internal/helpers/aitable.go:6896
visible_flags: 7

## Flags
- --base-id <String>: Base ID (必填)
- --scope <String>: 导出范围：all（整个 Base）、table（指定数据表）、view（指定视图）
- --export-format <String>: 导出格式：excel、attachment、excel_and_attachment、excel_with_inline_images
- --task-id <String>: 已有导出任务 ID，传入后继续等待（不要同时提供 scope/export-format/table-id/view-id）
- --table-id <String>: Table ID，scope=table 或 scope=view 时必填
- --view-id <String>: View ID，scope=view 时必填
- --timeout-ms <Int>: 单次等待超时（毫秒），默认 30000，最大 30000

## Related
- dws aitable import upload
