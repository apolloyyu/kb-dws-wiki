# dws contract import batch-result

kind: command
completeness: full
usage: dws contract import batch-result
description: 获取批量合同导入任务结果
example: dws contract import batch-result --task-id "task_xxx" --format json
source: internal/helpers/contract.go:223
visible_flags: 1

## Flags
- --task-id <String>: 批量导入任务 ID（必填，MCP getBatchImportContractResult 的 taskId）

## Related
- dws contract import batch
