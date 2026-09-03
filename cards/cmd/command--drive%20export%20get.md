# dws drive export get

kind: command
completeness: full
usage: dws drive export get
description: Query a Drive export task by task ID and return a normalized TaskResult.
example: dws drive export get --task-id <TASK_ID>
use_when: When the agent submitted an export with `--async` or the polling timed out and needs to check the export task.
source: internal/helpers/drive_export.go:445
visible_flags: 1

## Flags
- --task-id <String>: 导出任务 ID (必填)

## Related
- none
