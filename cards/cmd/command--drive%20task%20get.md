# dws drive task get

kind: command
completeness: full
description: Query an async task by ID and type (`export\
use_when: import\|copy\|move`) and return a normalized TaskResult. | When the agent needs the terminal state of an export/import/copy/move task after a timeout or interruption.
source: internal/helpers/drive.go:2333
visible_flags: 2

## Flags
- --type <String>: 任务类型: export|import|copy|move (必填)
- --id <String>: 任务 ID (必填)

## Related
- none
