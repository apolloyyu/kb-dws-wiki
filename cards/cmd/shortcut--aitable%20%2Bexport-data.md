# dws aitable +export-data

kind: shortcut
completeness: full
usage: dws aitable +export-data
description: 导出 AI 表格数据（创建导出任务或按 taskId 续等）
source: internal/shortcut/aitable/aitable.go:2583
visible_flags: 7

## Flags
- --base-id <String>: Base ID
- --task-id <String>: 已有导出任务 ID（传入则续等，不重新创建）
- --scope <String>: 导出范围
- --format <String>: 导出格式
- --table-id <String>: Table ID（scope=table/view 时）
- --view-id <String>: View ID（scope=view 时）
- --timeout-ms <Int>: 同步等待超时（毫秒，可选）

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
