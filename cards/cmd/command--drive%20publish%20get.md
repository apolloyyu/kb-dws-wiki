# dws drive publish get

kind: command
completeness: full
description: 查询单个异步任务状态
source: internal/helpers/drive.go:2333
visible_flags: 2

## Flags
- --type <String>: 任务类型: export|import|copy|move (必填)
- --id <String>: 任务 ID (必填)

## Related
- dws drive publish set
- dws drive publish unset
