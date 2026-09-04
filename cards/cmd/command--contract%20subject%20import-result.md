# dws contract subject import-result

kind: command
completeness: full
usage: dws contract subject import-result
description: 查询相对方批量导入结果
example: dws contract subject import-result --task-id "task_xxx" --format json
source: internal/helpers/contract.go:1504
visible_flags: 1

## Flags
- --task-id <String>: 导入任务 ID（必填）

## Related
- dws contract subject add
- dws contract subject auto-fill
- dws contract subject base-info
- dws contract subject batch-delete
- dws contract subject delete
- dws contract subject detail
