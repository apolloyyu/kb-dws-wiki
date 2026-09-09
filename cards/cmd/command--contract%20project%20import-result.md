# dws contract project import-result

kind: command
completeness: full
usage: dws contract project import-result
description: 获取项目批量导入结果
example: dws contract project import-result --task-id "task_xxx" --format json
source: internal/helpers/contract.go:1091
visible_flags: 1

## Flags
- --task-id <String>: 导入任务 ID（必填）

## Related
- dws contract project add
- dws contract project delete
- dws contract project detail
- dws contract project digests
- dws contract project export
- dws contract project import
