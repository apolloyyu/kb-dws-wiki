# dws sheet import get

kind: command
completeness: full
usage: dws sheet import get
description: 查询表格导入任务结果（手动兜底）
example: dws sheet import get --task-id <TASK_ID>
source: internal/helpers/sheet_import.go:111
visible_flags: 1

## Flags
- --task-id <String>: 导入任务 ID (必填)

## Related
- dws sheet import create
