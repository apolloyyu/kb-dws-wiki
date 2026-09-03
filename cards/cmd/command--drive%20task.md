# dws drive task

kind: command
completeness: full
usage: dws drive task
description: 异步任务状态查询（统一入口）
example: dws drive task get — 统一查询入口，支持 export/import/copy/move 多类型，返回归一化 TaskResult
source: internal/helpers/drive.go:2313
visible_flags: 0

## Flags
- none

## Related
- dws drive comment
- dws drive commit
- dws drive copy
- dws drive cover
- dws drive delete
- dws drive download
